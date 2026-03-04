from data_processing.services.relationLevelCalculator import relationLevelCalculator
from data_processing.models import EntityLink

#runs the relation level calculation and outputs a summary of it. For demo purposes, called manually
def runRelationCalculation():
    before = EntityLink.objects.filter(reportLink=None).count()

    relationLevelCalculator()

    after = EntityLink.objects.filter(reportLink=None).count()
    created_or_updated = after - before

    print("Relation level calculation is completed.")
    print(f"Accumulated entity links before: {before}")
    print(f"Accumulated entity links after: {after}")
    print(f"New accumulation links created: {max(created_or_updated, 0)}")
