import utils 
from utils import PATH_DATA
from mission import Mission
from pathlib import Path



if __name__ == "__main__":
    utils.create_repositories()
    utils.extract_tar_gz()
    utils.clean_empty_files()

    mission1 = Mission(Path.joinpath(PATH_DATA,"07","EM_31074_030_20200724_124739.xml").as_posix())
    mission2 = Mission(Path.joinpath(PATH_DATA,"07","EM_31074_030_20200725_083221.xml").as_posix())


    print(mission1._list_mission)
    print(mission2._nb_mesures)
    print(Mission.all_mission)
    print(Mission.total_nb_mesures())
