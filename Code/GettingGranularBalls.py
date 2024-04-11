# The file is called to generate the GBs by main function.
from scipy.io import loadmat
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.cluster import k_means


# The first split stage according to SD.
def splitting_ball(gb_list, L):
    # input:
    # gb_list is the list of GBs, where each element represents the array of all the samples in the GB.
    # L is the parameter used to set the minimum number of samples in GB.
    gb_list_new = []
    for gb in gb_list:
        if gb.shape[0] >= L:
            ball_1, ball_2 = kmeans_ball(gb)  # Split the GB using 2-means
            SD_original = get_SD(gb)  # Calculate the SD of the original GB

            if len(ball_1) == 0:  # The samples were all counted in ball_2
                gb_list_new.append(ball_2)
                continue
            elif len(ball_2) == 0:  # The samples were all counted in ball_1
                gb_list_new.append(ball_1)
                continue

            SD_k_1 = get_SD(ball_1)  # Calculate the SD of sub-GB 1
            SD_k_2 = get_SD(ball_2)  # Calculate the SD of sub-GB 2

            SD_child = SD_k_1 + SD_k_2  # Calculate the SD_child of sub-GBs

            # Splitting criterion
            if SD_child < SD_original:
                gb_list_new.extend([ball_1, ball_2])
            else:
                gb_list_new.append(gb)
        else:
            gb_list_new.append(gb)

    return gb_list_new


# Split GBs using 2-means.
def kmeans_ball(gb):
    # input:
    # gb is a array including all samples in the gb.
    data = gb[:, :-1]  # Delete serial number column
    cluster = k_means(X=data, init='k-means++', n_clusters=2)[1]  # Record are the results of clustering for each sample
    ball1 = gb[cluster == 0, :]
    ball2 = gb[cluster == 1, :]
    return [ball1, ball2]


# Calculate the Sum Distance SD of GBs.
def get_SD(gb):
    # input:
    # gb is a array including all samples in the gb.
    data = gb[:, :-1]  # Delete serial number column
    center = data.mean(0)
    SD = np.sum(((data - center) ** 2).sum(axis=1) ** 0.5)
    return SD


# Calculate the radius and center of the GB
def get_radiusAndcenter(gb):
    # input:
    # gb is a array including all samples in the gb.
    data = gb[:, :-1]  # Delete serial number column
    center = data.mean(0)
    radius = np.mean(((data - center) ** 2).sum(axis=1) ** 0.5)
    return radius, center


# The second split stage, splitting some GBs with larger radius#
def Radius_big_split(gb_list, radius_detect):
    # input:
    # gb_list is the list of GBs, where each element represents the array of all the samples in the GB.
    # radius_detect is the splitting threshold for the radius of the GB.
    gb_list_temp = []
    for gb in gb_list:
        radius, _ = get_radiusAndcenter(gb)  # Get the radius of the GB.
        if len(gb) < 2:
            gb_list_temp.append(gb)
        else:
            if radius <= radius_detect:
                gb_list_temp.append(gb)
            else:
                ball_1, ball_2 = kmeans_ball(gb)  # Split the GB with larger radius
                gb_list_temp.extend([ball_1, ball_2])
    return gb_list_temp


def GettingGranularBalls(data_name, L):
    # input:
    # data_name is the name of the dataset;
    # L is the parameter used to set the minimum number of samples in GB.
    df = loadmat(r"datasets\\" + data_name)
    data = df['trandata'][:, :-1]  # data
    target = df['trandata'][:, -1]  # label

    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)

    # Join index in last column
    index = np.arange(0, data.shape[0], 1)
    data_index = np.insert(data, data.shape[1], values=index, axis=1)  # Add index to last column for each sample.
    gb_list_temp = [data_index]  # Start by treating the entire dataset as a GB.

    # The first split until the number of GBs no longer changes.
    while 1:
        ball_number_last = len(gb_list_temp)
        gb_list_temp = splitting_ball(gb_list_temp, L)
        ball_number_new = len(gb_list_temp)
        if ball_number_new == ball_number_last:
            break

    # Calculate radius threshold
    radius_list = []
    for gb in gb_list_temp:
        if len(gb) >= 2:
            radius, _ = get_radiusAndcenter(gb)
            radius_list.append(radius)
    radius_median = np.median(radius_list)  # Median radius
    radius_mean = np.mean(radius_list)  # Mean radius
    radius_detect = 2 * max(radius_median, radius_mean)

    # The second split until the number of GBs no longer changes.
    while 1:
        ball_number_old = len(gb_list_temp)
        gb_list_temp = Radius_big_split(gb_list_temp, radius_detect)
        ball_number_new = len(gb_list_temp)
        if ball_number_new == ball_number_old:
            break

    # Count the radius and center of each GB.
    radius_list = []
    center_list = []
    for gb in gb_list_temp:
        mean_radius, center = get_radiusAndcenter(gb)
        center_list.append(center)
        radius_list.append(mean_radius)

    # Get the final GB list.
    gb_list_final = gb_list_temp

    return target, data, gb_list_final, radius_list, center_list
