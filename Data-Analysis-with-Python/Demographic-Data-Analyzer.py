import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('C:\\Belajar Kode\\FreeCodeCamp\\Data Analytics\\adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    race_count = race_count.tolist()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    average_age_men = average_age_men.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    education_total = df['education'].count()
    bachelor_total = df['education'].value_counts().get('Bachelors', 0)
    percentage_bachelors = (bachelor_total/education_total) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']).eq(False)]

    # percentage with salary >50K
    advanced_education_above50 = higher_education[higher_education['salary'] == '>50K']
    percentage_above_edu_50 = ((len(advanced_education_above50) / len(higher_education)) * 100)
    higher_education_rich = round(percentage_above_edu_50, 1)
    
    low_edu_above50 = lower_education[lower_education['salary'] == '>50K']
    percentage_low_edu = (len(low_edu_above50) / len(lower_education) * 100)
    lower_education_rich = round(percentage_low_edu, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]
    min_worker_50k = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = (len(min_worker_50k) / len(num_min_workers)) * 100

    # What country has the highest percentage of people that earn >50K?
    highsalary = df[df['salary'] == '>50K']
    countrygroup = highsalary.groupby('native-country')
    percentage_by_country = (countrygroup.size() / df.groupby('native-country').size()) * 100
    highest_earning_country = percentage_by_country.idxmax()
    highest_earning_country_percentage = percentage_by_country.max().round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    salary_high_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    popular_occupation = salary_high_india['occupation'].value_counts()
    top_IN_occupation = popular_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
