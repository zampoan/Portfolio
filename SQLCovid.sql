--Select Data that we will be using
SELECT
	location, date, total_cases, new_cases, total_deaths, population
FROM 
	PortfolioProject..CovidDeaths$
ORDER BY location, date

-- Total Cases vs. Total deaths
SELECT
	location, date, total_cases, total_deaths, population, (total_deaths/total_cases)*100 AS death_percentage 
FROM 
	PortfolioProject..CovidDeaths$
WHERE 
	location LIKE '%Australia%'
ORDER BY 
	location, date

--Total Cases vs Population
SELECT
	location, total_cases, population, (total_cases/population) AS case_per_pop
FROM
	PortfolioProject..CovidDeaths$
WHERE
	location LIKE '%Australia%'
ORDER BY
	1

-- Look at countries with highest infection rate compared with population
SELECT
	location,  population, MAX(total_cases) AS highest_infection_count, MAX((total_cases/population)) * 100 AS percent_pop_infected
FROM
	PortfolioProject..CovidDeaths$
GROUP BY
	location, population
ORDER BY
	location, population

-- Look at how many people died by location
SELECT
	location, population, MAX(cast(total_deaths AS INT)) AS total_deaths 
FROM 
	PortfolioProject..CovidDeaths$
WHERE
	continent IS NOT NULL
GROUP BY
	location, population
ORDER BY
	3 DESC

-- look at how many people died by continent
SELECT
	continent, MAX(cast(total_deaths AS INT)) AS total_deaths 
FROM 
	PortfolioProject..CovidDeaths$
WHERE
	continent IS NOT NULL
GROUP BY
	continent
ORDER BY
	total_deaths DESC


-- Total Population vs Vaccination
-- Rolling Count
SELECT
	dea.continent, dea.location, dea.date, population, vac.new_vaccinations, 
	SUM(CAST(vac.new_vaccinations as INT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as rolling_people_vacc
FROM PortfolioProject..CovidDeaths$ dea
JOIN PortfolioProject..CovidVaccinations$ vac
	ON dea.location = vac.location AND dea.date = vac.date
WHERE
	dea.continent IS NOT NULL
ORDER BY 
	1, 2, 3





-- Use CTE for above problem
WITH PopVsVac(continent, location, date, population, new_vaccinations,rolling_people_vacc)
AS
(SELECT
	dea.continent, dea.location, dea.date, population, vac.new_vaccinations, 
	SUM(CAST(vac.new_vaccinations as INT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as rolling_people_vacc
FROM PortfolioProject..CovidDeaths$ dea
JOIN PortfolioProject..CovidVaccinations$ vac
	ON dea.location = vac.location AND dea.date = vac.date
WHERE
	dea.continent IS NOT NULL
)
SELECT 
	*, (rolling_people_vacc/population) * 100
FROM
	PopVsVac





--TEMP TABLE

DROP TABLE IF EXISTS PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
continent varchar(255), location varchar(255), date datetime, population numeric, new_vaccinations numeric, rolling_people_vacc numeric)

INSERT INTO #PercentPopulationVaccinated
SELECT
	dea.continent, dea.location, dea.date, population, vac.new_vaccinations, 
	SUM(CAST(vac.new_vaccinations as INT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as rolling_people_vacc
FROM PortfolioProject..CovidDeaths$ dea
JOIN PortfolioProject..CovidVaccinations$ vac
	ON dea.location = vac.location AND dea.date = vac.date
WHERE
	dea.continent IS NOT NULL

SELECT 
	*, (rolling_people_vacc/population) * 100
FROM
	#PercentPopulationVaccinated

	

-- CREATING VIEW TO STORE DATA FOR LATER VISUALIZATIONS
CREATE VIEW PercentPopulationVaccinated as 
SELECT
	dea.continent, dea.location, dea.date, population, vac.new_vaccinations, 
	SUM(CAST(vac.new_vaccinations as INT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as rolling_people_vacc
FROM PortfolioProject..CovidDeaths$ dea
JOIN PortfolioProject..CovidVaccinations$ vac
	ON dea.location = vac.location AND dea.date = vac.date
WHERE
	dea.continent IS NOT NULL





	