from django.db import models

# User Table
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # admin / agent
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"


# Raw Material Table
class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    purity = models.FloatField()

    def __str__(self):
        return f"{self.name} | Purity: {self.purity}%"


# Material Table
class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    predicted_yield = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} | Qty: {self.quantity}"


# Process Result Table
class ProcessResult(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    red_mud = models.FloatField()
    digestion_temp = models.FloatField()
    digestion_pressure = models.FloatField()
    naoh_concentration = models.FloatField()
    residence_time = models.FloatField()
    precipitation_temp = models.FloatField()
    precipitation_pressure = models.FloatField()
    calcination_temp = models.FloatField()
    aluminum_yield = models.FloatField()
    energy_consumption = models.FloatField()
    co2_emissions = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # ✅ helps identify records

    def __str__(self):
        return (
            f"ID:{self.id} | {self.material.name} | "
            f"Yield:{self.aluminum_yield} | Temp:{self.digestion_temp}"
        )


# Test Data Table
class TestData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.value})"