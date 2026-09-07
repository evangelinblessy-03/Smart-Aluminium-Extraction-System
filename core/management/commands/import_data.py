import pandas as pd
from django.core.management.base import BaseCommand
from core.models import ProcessResult, Material
from pathlib import path

class Command(BaseCommand):
    help = "Import aluminum dataset"

    def handle(self, *args, **kwargs):
        BASE_DIR = Path(__file__).resolve().parents[4]
        DATA_FILE = BASE_DIR / "data" / "aluminum_extraction_dataset.csv"

        df = pd.read_csv(DATA_FILE)

        for _, row in df.iterrows():
            material = Material.objects.create(
                name="Bauxite",
                quantity=100
            )

            ProcessResult.objects.create(
                material=material,
                red_mud=0,
                digestion_temp=row["Digestion_Temp_C"],
                digestion_pressure=row["Digestion_Pressure_bar"],
                naoh_concentration=row["NaOH_Concentration_gpl"],
                residence_time=row["Residence_Time_hr"],
                precipitation_temp=row["Precipitation_Temp_C"],
                precipitation_pressure=1,
                calcination_temp=row["Calcination_Temp_C"],
                aluminum_yield=row["Alumina_Yield_%"],
                energy_consumption=row["Energy_Consumption_kWh_per_ton"],
                co2_emissions=row["CO2_Emissions_ton_per_ton"]
            )

        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))