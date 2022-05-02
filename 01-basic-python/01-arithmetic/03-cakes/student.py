# Write your code here
def cakes(eggs,butter,flour):
    maxByEggs = eggs//5
    maxByButter = butter // 250
    maxByFlour = flour // 5

    return min(maxByEggs, maxByButter, maxByFlour)