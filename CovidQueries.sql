/*
Queries for Tableau project
*/

--1. Find total number of cases, with total deaths and percentage of people who died

SELECT 
	SUM(new_cases) AS total_cases, SUM(cast(new_deaths AS INT)) AS total_deaths, 
	SUM(cast(new_deaths AS INT))/SUM(new_cases) * 100 AS DeathPercentage
FROM
	PortfolioProject..CovidDeaths$
WHERE
	continent IS NOT NULL
ORDER BY
	1, 2

--2. Total number of deaths in each country
SELECT 
	continent, SUM(CAST(new_deaths AS INT)) AS TotalDeathCount
FROM
	PortfolioProject..CovidDeaths$
WHERE
	continent IS NOT NULL AND location NOT IN ('World', 'European Union', 'International')
GROUP BY
	continent
ORDER BY
	TotalDeathCount DESC

--3. Country and population with highest number of cases and percentage of population that has been infected
SELECT
	location, population, MAX(total_cases) AS HighestInfectionCount, MAX(total_cases/population)*100 as PercentPopulationInfected
FROM
	PortfolioProject..CovidDeaths$
GROUP BY 
	location, population
ORDER BY
	PercentPopulationInfected DESC

--4. Same as above but include date
SELECT
	location, population, date, MAX(total_cases) AS HighestInfectionCount, MAX(total_cases/population)*100 as PercentPopulationInfected
FROM
	PortfolioProject..CovidDeaths$
GROUP BY 
	location, population, date
ORDER BY
	PercentPopulationInfected DESC


