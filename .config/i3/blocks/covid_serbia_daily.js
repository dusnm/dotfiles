/**
 * @author Dusan Mitrovic <dusan@dusanmitrovic.xyz>
 * @license GNU General Public License, version 3 only
 *
 * A script to fetch the latest statistics for covid-19 in Serbia
 */
const COVID19_API_DATA_URL = 'https://covid19.data.gov.rs/api/datasets/statistic/official';
const NEW_CASES_CODE = 'BROJ_POZITIVNIH_LICA_ZA_DATI_DATUM';
const NUMBER_OF_TESTED_PEOPLE_CODE = 'BROJ_TESTIRANIH_LICA_ZA_DATI_DATUM';
const NUMBER_OF_DEAD_PEOPLE_CODE = 'BROJ_PREMINULIH_LICA_ZA_DATI_DATUM';

fetch(COVID19_API_DATA_URL)
 .then(response => response.json())
 .then(data => {
     const new_cases = data.filter(item => item.dataCode === NEW_CASES_CODE);
     const number_of_tested_people = data.filter(item => item.dataCode === NUMBER_OF_TESTED_PEOPLE_CODE);
     const number_of_dead_people = data.filter(item => item.dataCode === NUMBER_OF_DEAD_PEOPLE_CODE);

     const new_cases_today = new_cases[0].points[new_cases[0].points.length - 1].ordinate;
     const number_of_tested_people_today = number_of_tested_people[0].points[number_of_tested_people[0].points.length - 1].ordinate;
     const number_of_dead_people_today = number_of_dead_people[0].points[number_of_dead_people[0].points.length - 1].ordinate;
    
     console.log(`🧪 ${number_of_tested_people_today} 🤧 ${new_cases_today} 💀 ${number_of_dead_people_today}`);
 });
