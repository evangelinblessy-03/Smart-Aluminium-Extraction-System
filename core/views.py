from django.shortcuts import render, redirect
from .models import RawMaterial, ProcessResult, User, Material


# ── Home Page ──────────────────────────────────────────────
def home(request):
    return render(request, 'home.html')


# ── Register ───────────────────────────────────────────────
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role') or 'user'

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})

        User.objects.create(username=username, password=password, role=role)
        return redirect('user_login')

    return render(request, 'register.html')


# ── User Login ─────────────────────────────────────────────
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username, password=password, role='user').first()
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['role'] = 'user'
            return redirect('dashboard')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid credentials or not a user account'})

    return render(request, 'user_login.html')


# ── Admin Login ────────────────────────────────────────────
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username, password=password, role='admin').first()
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['role'] = 'admin'
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials or not an admin account'})

    return render(request, 'admin_login.html')


# ── Admin Dashboard ────────────────────────────────────────
def admin_dashboard(request):
    if not request.session.get('user_id'):
        return redirect('admin_login')
    if request.session.get('role') != 'admin':
        return redirect('user_login')

    total_results   = ProcessResult.objects.count()
    total_materials = Material.objects.count()
    total_users     = User.objects.filter(role='user').count()
    recent_results  = ProcessResult.objects.select_related('material').order_by('-created_at')[:10]

    return render(request, 'admin_dashboard.html', {
        'username':        request.session.get('username'),
        'total_results':   total_results,
        'total_materials': total_materials,
        'total_users':     total_users,
        'recent_results':  recent_results,
    })


# ── User Dashboard ─────────────────────────────────────────
def dashboard(request):
    if not request.session.get('user_id'):
        return redirect('user_login')
    return render(request, 'dashboard.html', {'username': request.session.get('username')})





# ── Add Material + Process ─────────────────────────────────
def add_material(request):
    if not request.session.get('user_id'):
        return redirect('user_login')

    if request.method == 'POST':
        name   = request.POST.get('name')
        weight = request.POST.get('weight')
        purity = request.POST.get('purity')

        if name and weight and purity:
            weight = float(weight)
            purity = float(purity)

            aluminum = round(weight * (purity / 100), 4)
            red_mud  = round(weight - aluminum, 4)

            RawMaterial.objects.create(name=name, weight=weight, purity=purity)

            material = Material.objects.create(
                name=name,
                quantity=int(weight),
                predicted_yield=aluminum,
            )

            result = ProcessResult.objects.create(
                material=material,
                red_mud=red_mud,
                digestion_temp=0.0,
                digestion_pressure=0.0,
                naoh_concentration=0.0,
                residence_time=0.0,
                precipitation_temp=0.0,
                precipitation_pressure=0.0,
                calcination_temp=0.0,
                aluminum_yield=aluminum,
                energy_consumption=0.0,
                co2_emissions=0.0,
            )

            request.session['result_id'] = result.id

            return render(request, 'results.html', {
                'aluminum': aluminum,
                'red_mud':  red_mud,
                'name':     name,
            })

    return render(request, 'add_material.html')


# ── View Results ───────────────────────────────────────────
def view_results(request):
    result_id = request.session.get('result_id')

    if result_id:
        try:
            result = ProcessResult.objects.get(id=result_id)
            return render(request, 'results.html', {
                'name':     result.material.name,
                'aluminum': result.aluminum_yield,
                'red_mud':  result.red_mud,
            })
        except ProcessResult.DoesNotExist:
            pass

    return render(request, 'results.html', {'error': 'No results found'})


# ── Logout ─────────────────────────────────────────────────
def logout_view(request):
    role = request.session.get('role')
    request.session.flush()
    if role == 'admin':
        return redirect('admin_login')
    return redirect('user_login')


# ── Result History ─────────────────────────────────────────
def result_history(request):
    if not request.session.get('user_id'):
        return redirect('user_login')

    query = request.GET.get('q')
    if query:
        results = ProcessResult.objects.filter(material__name__icontains=query)
    else:
        results = ProcessResult.objects.all()

    return render(request, 'history.html', {'results': results})
