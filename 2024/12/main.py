import sys
import numpy as np


def main(file_name: str):
    farm_map = get_input(file_name)
    plants = np.unique(farm_map)
    total_cost = 0
    total_disc_cost = 0
    for plant in plants:
        plots = np.argwhere(farm_map == plant)
        plant_regions = con_components(plots)
        costs = [get_cost(region) for region in plant_regions]
        total_cost += sum(costs)
        disc_cost = [get_discounted_cost(region) for region in plant_regions]
        total_disc_cost += sum(disc_cost)
        # total_cost += get_cost(plots)
    print("Part 1: ", total_cost)
    print("Part 2: ", total_disc_cost)


def con_components(plots: np.array) -> list[np.array]:
    regions = []
    unaccounted_plots = np.copy(plots)
    while len(unaccounted_plots) > 0:
        start_plot = unaccounted_plots[0]
        unaccounted_plots = unaccounted_plots[1:]
        region, unaccounted_plots = expand(
            np.array([start_plot]),
            unaccounted_plots
        )
        regions.append(region)
    return regions


def get_discounted_cost(region):
    sides = len(get_sides(region))
    area = len(region)
    return area*sides


def get_boundary(region: np.array) -> np.array:
    # add a direction coord
    bdry = np.empty((0, 3), dtype=int)
    up = np.array([-1, 0], dtype=int)
    down = np.array([1, 0], dtype=int)
    left = np.array([0, -1], dtype=int)
    right = np.array([0, 1], dtype=int)
    for plot in region:
        if ~(region == plot + up).all(1).any():
            bdry = np.vstack((bdry, np.append(plot + up, 0)))
        if ~(region == plot + right).all(1).any():
            bdry = np.vstack((bdry, np.append(plot + right, 1)))
        if ~(region == plot + down).all(1).any():
            bdry = np.vstack((bdry, np.append(plot + down, 2)))
        if ~(region == plot + left).all(1).any():
            bdry = np.vstack((bdry, np.append(plot + left, 3)))
    return bdry


def get_sides(region: np.array) -> list[np.array]:
    bdry = get_boundary(region)
    sides = []
    while len(bdry) > 0:
        inSide = True
        side = np.array([bdry[0]], dtype=int)
        bdry = bdry[1:]
        side_type = side[0][2]
        while inSide:
            if side_type % 2 == 0:
                neighR = side[-1] + [0, 1, 0]
                neighL = side[0] + [0, -1, 0]
                inSide = False
                if (bdry == neighR).all(1).any():
                    inSide = True
                    side = np.vstack((side, neighR))
                    bdry = bdry[~(bdry == neighR).all(1)]
                if (bdry == neighL).all(1).any():
                    inSide = True
                    side = np.vstack((neighL, side))
                    bdry = bdry[~(bdry == neighL).all(1)]
            else:
                neighU = side[0] + [-1, 0, 0]
                neighD = side[-1] + [1, 0, 0]
                inSide = False
                if (bdry == neighU).all(1).any():
                    inSide = True
                    side = np.vstack((neighU, side))
                    bdry = bdry[~(bdry == neighU).all(1)]
                if (bdry == neighD).all(1).any():
                    inSide = True
                    side = np.vstack((side, neighD))
                    bdry = bdry[~(bdry == neighD).all(1)]
        sides.append(side)
    return sides


def expand(plots: np.array, region: np.array) -> np.array:
    if len(region) == 0:
        return plots, region
    isConnected = True
    while isConnected:
        tot_neighs = np.empty((0, 2), dtype=int)
        for plot in plots:
            neigh = get_neigh(plot, region)
            tot_neighs = np.vstack((tot_neighs, neigh))
            region = region[~(region == plot).all(1)]
            for nplot in neigh:
                region = region[~(region == nplot).all(1)]
        tot_neighs = np.unique(tot_neighs, axis=0)
        plots = np.vstack((plots, tot_neighs))
        isConnected = len(tot_neighs) > 0
    return plots, region


def get_cost(region: np.array) -> int:
    area = len(region)
    perimeter = 0
    curr_region = np.empty((0, 2), dtype=int)
    for plot in region:
        n = len(get_neigh(plot, curr_region))
        perimeter += 4 - 2*n
        curr_region = np.vstack((curr_region, plot))
    return area*perimeter


def get_neigh(plot: np.array, region: np.array) -> np.array:
    neighbors = np.empty((0, 2), dtype=int)
    pos_neigh = [
        plot + (1, 0),
        plot + (-1, 0),
        plot + (0, 1),
        plot + (0, -1)
    ]
    for neigh in pos_neigh:
        if (neigh == region).all(1).any():
            neighbors = np.vstack((neighbors, neigh))
    return neighbors


def get_input(file_name: str) -> np.array:
    with open(file_name) as f:
        lines = f.readlines()
        arr = np.array([list(line.strip()) for line in lines])
    return arr


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('sample.txt')
    else:
        main('input.txt')
