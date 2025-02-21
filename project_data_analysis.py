# Excedding requirements:
# 1. Identify the year and country that had the biggest drop in life expectancy from one year to the next.

with open("life-expectancy.csv") as life_expec:
    high_expectancy = float('-inf')
    low_expectancy = float('inf')
    high_entity = high_year = ""
    low_entity = low_year = ""

    next (life_expec)

    choose = input("Enter the year of interest: ")

    # Variable
    total_life_expectancy = 0
    count = 0
    min_life_expec_year = float('inf')
    max_life_expec_year = float('-inf')
    min_country_year = ""
    max_country_year = ""

    # Variables for excedding requeriments
    previous_life_expectancy = {}
    largest_drop = 0
    drop_country = ""
    drop_year = 0

    for expectation in life_expec:
        parts = expectation.split(",")
        if len(parts) == 4:
            entity, code, year, life = parts
            life = float(life)
            year = int(year)

            # Calculating overall min and max life expectancy
            if life > high_expectancy:
                high_expectancy = life
                high_entity = entity
                high_year = year 

            if life < low_expectancy:
                low_expectancy = life
                low_entity = entity
                low_year = year 

            # Calculating life expectancy for the chosen year
            if year == int(choose):
                total_life_expectancy += life
                count += 1

                if life < min_life_expec_year:
                    min_life_expec_year = life
                    min_country_year = entity 

                if life > max_life_expec_year:
                    max_life_expec_year = life
                    max_country_year = entity
                    
                    
            # Calculating the largest drop
            if entity in previous_life_expectancy:
                previous_life = previous_life_expectancy[entity][0]
                drop = previous_life - life  
                if drop > largest_drop:
                    largest_drop = drop
                    drop_country = entity
                    drop_year = year 

            previous_life_expectancy[entity] = (life, year)

# Print statistics for the chosen year
if count > 0:
    average_life_expec_year = total_life_expectancy / count
    print(f"The overall max life expectancy is: {high_expectancy} from {high_entity} in {high_year}")
    print(f"The overral min life expectancy is: {low_expectancy} from {low_entity} in {low_year}")
    
    print()
    
    print(f"For the year {choose}:")
    print(f"The averange life expectancy across all countries was {average_life_expec_year:.2f}")
    print(f"The max life expectancy was in {max_country_year} with {max_life_expec_year:.2f}")
    print(f"The min life expectancy was is {min_country_year} with {min_life_expec_year:.2f}")
    
    print()

    # Print the largest drop in life expectancy
    print(f"The largest drop in life expectancy was {largest_drop:.2f} years in {drop_year - 1} to {drop_year}")

else:
    print(f"No data available for the year {choose}")



      

        

