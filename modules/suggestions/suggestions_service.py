import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from modules.interactions.interactions_repository import InteractionsRepository
from modules.movies.movies_repository import MoviesRepository
from modules.tags.tags_repository import TagsRepository

class SuggestionsService:
    def __init__(self, movies_repository: MoviesRepository, repository_interactions: InteractionsRepository, repository_tags: TagsRepository):

        self.movies_repository = movies_repository
        self.repository_interactions = repository_interactions
        self.repository_tags = repository_tags
        

    def generate_suggestions(self,user_id):

        data = self.repository_interactions.get_all_interactions(user_id)
        if not data:
            return []

        data_formatted = [{'tag_id': d.tag_id, 'weight': d.weight} for d in data]

        df_complete = pd.DataFrame(data_formatted)

        
        tag_ids = df_complete['tag_id'].tolist()
        movies_with_tags = self.movies_repository.get_movies_by_tags(tag_ids)
    
        movies_data = []
        for movie in movies_with_tags:
            for tag in movie.tags:
                movies_data.append({'movie_id': movie.id, 'tag_id': tag.id, 'title': movie.title})
    
        df_movies = pd.DataFrame(movies_data)

        
        df_suggestions = pd.merge(df_movies, df_complete, on='tag_id')

        
        ranking = df_suggestions.groupby(['movie_id', 'title'])['weight'].sum().reset_index()

        top_10 = ranking.sort_values(by='weight', ascending=False).head(10)

        # Falta implementar o salvar no banco

        return top_10.to_dict(orient='records')