#!pip install n2
from n2 import HnswIndex
import pandas as pd


class music_recommendation():
    def __init__(self):
        self.m_index = HnswIndex(57)
        # 저장된 인덱스 호출
        self.m_index.load('./content/six_genre_index.hnsw')

        # 음악 추출 데이터 호출
        music_feature = pd.read_csv('./content/six_genre_music.csv',
            index_col=None)

        # 6가지 감정만 사용
        selected_music = music_feature[(music_feature['labels'] == 'Happy') | (music_feature['labels'] == 'Angry') | (
                    music_feature['labels'] == 'Sad') | (music_feature['labels'] == 'Calm') | (
                                                   music_feature['labels'] == 'Dramatic') | (
                                                   music_feature['labels'] == 'Dark')]
        selected_music.reset_index(inplace=True, drop=True)

        self.index_and_music = {i: k for i, k in enumerate(selected_music['music_names'])}

    def recommendation_by_id(self, id):
        # 0~119 : Angry
        if id in range(0, 120):
            music_mood = 'Angry'
            music_range = range(0, 120)
            music_list = [musics for musics in self.m_index.search_by_id(id, 720) if musics in music_range]
        # 120~239 : Happy
        elif id in range(120, 240):
            music_mood = 'Happy'
            music_range = range(120, 240)
            music_list = [musics for musics in self.m_index.search_by_id(id, 720) if musics in music_range]
        # 240~359 : Calm
        elif id in range(240, 360):
            music_mood = 'Calm'
            music_range = range(240, 360)
            music_list = [musics for musics in self.m_index.search_by_id(id, 720) if musics in music_range]
        # 360~479 : Dark
        elif id in range(360, 480):
            music_mood = 'Dark'
            music_range = range(360, 480)
            music_list = [musics for musics in self.m_index.search_by_id(id, 720) if musics in music_range]
        # 480~599 : Sad
        elif id in range(480, 600):
            music_mood = 'Sad'
            music_range = range(480, 600)
            music_list = [musics for musics in self.m_index.search_by_id(id, 720) if musics in music_range]
        # 600~719 : Dramatic
        elif id in range(600, 720):
            music_mood = 'Dramatic'
            music_range = range(600, 720)
            music_list = [musics for musics in self.m_index.search_by_id(id, 720) if musics in music_range]

        return music_mood, [self.index_and_music[recomend_music] for recomend_music in music_list[1:6]]
