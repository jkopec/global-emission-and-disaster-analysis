## Analysis of global emissions and natural disasters

## Description
The aim of this work is to analyze the interaction between global CO2 emissions and natural disasters from 1960 to 2021. 

For this purpose, two different datasets are used as input data. The information on CO2 emissions for each country over the years comes from the Global Carbon Atlas. The information on natural disasters and their region over the years comes from EM-DAT, a global database of natural and technological disasters, although only the former is considered in this work. 

These input datasets will be filtered and combined to create a new dataset that will provide a holistic view of the situation and illustrate the relationship between CO2 emissions and natural disasters.

## Results / Output

- CSV file containing data about global CO2 emissions in Mt and number of natural disasters per year
  - Link: [CSV](out/worldwide_CO2_emissions_and_natural_disasters_1960_to_2021.csv)
- PDF file containing a plot visualizing the CSV-Data
  - Link: [PDF](out/worldwide_CO2_emissions_and_natural_disasters_1960_to_2021.pdf)


## Installation
In order to use this repository, the following requirements need to be fulfilled.
### Requirements
- clone this repository
- install python for your platform >=3.10
- install all python modules mentioned in [src/requirements.txt](src/requirements.txt)
  ```bash
  pip install -r requirements.txt
  ```

## Usage
To recreate the results / output data, simply run the [src/plot.py] script after you fulfilled all requirements of the [Installation](#installation) section.

```bash
python src/plot.py
```

The output data can then be found in the [out/](out/) folder.

## Support
If you have questions/suggestions about the source code in this project, feel free to create an Issue and I will answer it as soon as possible.

If you have questions about the input data I would like to kindly guide you to one of the following sources:

- Global Carbon Atlas
  - DOI: http://doi.org/10.17616/R3434K
  - URL: http://www.globalcarbonatlas.org/en/CO2-emissions
  - Last accessed: 2023-05-09 
- EM-DAT
  - DOI: http://doi.org/10.17616/R3QQ1X
  - URL: https://public.emdat.be/data (registration necessary)
  - Last accessed: 2023-05-14

If you think that the data I used in [res/](res/) is somehow not correct, please also create an Issue.
## Roadmap
This project deals only very superficially with this topic. The input data offer much more possibilities for analysis, but due to time constraints they could not be considered so far. 

In the future, for example, it could be analyzed how the number of fatalities or the financial damages caused by natural disasters have behaved over the years in comparison to global CO2 emissions. 

It might be interesting to have a more detailed analysis at country level, showing which countries are the biggest victims of natural disasters and whether this correlates with the CO2 emissions of these countries.

On the technical side of things, it would be nice to have an automation which downloads the input data from the respective sources and prepares it so that the headers and footers are removed so that the python script can be executed right away. However this might get tedious because EM-DAT requires user authentication in order to download data.

## Contributing
I am open to contributions. There are no specific requirements you have to fulfill as long as the data you are providing is cited and comes from a valid source and the code in this project has no compile or runtime errors, is commented and formatted according to a particular standard for the programming language in use.

## Authors and acknowledgment
This project is created and maintained by [Jakub Kopec](https://orcid.org/0009-0006-8549-5031). The input data used for this project under [res/](res/) come from [Global Carbon Atlas](http://doi.org/10.17616/R3434K) and [EM-DAT](http://doi.org/10.17616/R3QQ1X).

## License
The [source code](src/) and [ouput](out/) of this project is licenced with the MIT license.

However, the [input data](res/) needs to be cited according to the valid sources and used only according to the license agreements of those sources!

## Project status
The project will probably not be maintained after 14.05.2023. If you want to become the maintainer or owner of this project, please contact me: jakub.kopec(at)student.tuwien.ac.at.