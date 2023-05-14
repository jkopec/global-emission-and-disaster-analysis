import os
import pandas as pd
import matplotlib.pyplot as plt

# get directory of current script
script_dir = os.path.dirname(os.path.abspath(__file__))


def get_worldwide_co2_emissions():
    # construct path to data source (global carbon atlas export)
    data_src = os.path.join(script_dir, '..', 'res', 'co2_emissions',
                            'mtco2_1960-2021.csv')

    # read in data from the global carbon atlas
    df = pd.read_csv(data_src, delimiter=';')

    # select columns for summation (excluding the first column)
    columns_to_sum = df.columns[1:]

    # sum up the total emissions of every country per year
    total_emissions = df[columns_to_sum].sum(axis=1)

    # create a new DataFrame with 'Year' column and total emissions
    result = pd.DataFrame({
        'Year': df['Year'],
        'Emissions MtCO2': total_emissions
    })

    return result


def worldwide_natural_disasters():
    # construct path to data source (global carbon atlas export)
    data_src = os.path.join(script_dir, '..', 'res', 'natural_disasters',
                            'emdat_public_2023_05_10_query_uid-EgWcRx.xlsx')

    # read in data from the global carbon atlas
    df = pd.read_excel(data_src)

    # calculate total disasters per year and resulting deaths
    result = df.groupby('Year').agg(Disasters=('Year', 'size')).reset_index()

    # restricting the dataset to only use data between 1960 and 2021
    result = result.query('Year >= 1960 and Year <= 2021')

    return result


def export(filename=None, data_frame=None, plot=None):
    if filename is None:
        return

    # construct path to output directory
    output_dir = os.path.join(script_dir, '..', 'out')

    # make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # construct output path for file
    output_path = os.path.join(output_dir, filename)

    if filename.endswith('.csv') and data_frame is not None:

        # export DataFrame to CSV file
        data_frame.to_csv(output_path, index=False)

    elif filename.endswith('.pdf') and plot is not None:

        # export plot to PDF file
        plot.savefig(output_path)
        # clear the object
        plot.clf()

    else:
        return


def plot(data_frame, x1_data, y1_data, y2_data, x1_label, y1_label, y2_label,
         y1_color, y2_color, title):

    if data_frame is None:
        return

    # Create a figure and axis objects
    fig, ax1 = plt.subplots()

    # Plot the first dataset on the primary y-axis
    ax1.plot(
        data_frame[x1_data],
        data_frame[y1_data],
        color=y1_color,
        label=y1_label,
    )

    ax1.set_xlabel(x1_label)
    ax1.set_ylabel(y1_label)

    # Create a secondary y-axis
    ax2 = ax1.twinx()

    # Plot the second dataset on the secondary y-axis
    ax2.plot(
        data_frame[x1_data],
        data_frame[y2_data],
        color=y2_color,
        label=y2_label,
    )

    ax2.set_ylabel(y2_label)

    # Add a legend
    fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85))

    # Add a title
    plt.title(title)

    return plt


if __name__ == '__main__':
    # get DataFrame about worldwide CO2 emissions
    emissions = get_worldwide_co2_emissions()
    # get DataFrame about worldwide natural disasters
    disasters = worldwide_natural_disasters()

    # merge both values together into a single DataFrame
    result = pd.merge(emissions, disasters, on='Year')

    # export all data as CSV file
    export(data_frame=result,
           filename=
           'worldwide_CO2_emissions_and_natural_disasters_1960_to_2021.csv')

    # plot emissions and disasters
    emissions_and_disasters = plot(
        data_frame=result,
        x1_data='Year',
        x1_label='Year',
        y1_data='Emissions MtCO2',
        y1_label='$\mathrm{CO_{2}}$ emissions in Mt',
        y1_color='red',
        y2_data='Disasters',
        y2_label='# of natural disasters',
        y2_color='blue',
        title='Worldwide $\mathrm{CO_{2}}$ emissions' +
        ' and natural disasters (1960-2021)',
    )

    # export plot to PDF
    export(plot=emissions_and_disasters,
           filename=
           'worldwide_CO2_emissions_and_natural_disasters_1960_to_2021.pdf')
