from scipy.stats import binned_statistic

class data_manipulation:

    def bin_numerical_data(column):
        bins = binned_statistic(column, [30, 60, 90, 120, 150], bins = 5)
        return bins
    
    def parse_binned_statistic(bin_tuple, column):
        bin_numbers = bin_tuple[2]
        binned_zipped_list = zip(bin_numbers, column)
        return binned_zipped_list

