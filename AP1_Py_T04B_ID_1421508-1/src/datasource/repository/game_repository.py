from datasource.mapper.game_mapper import GameMapper


class GameRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.mapper = GameMapper()
    
    def save(self, game):
        session = self.session_factory()
        try:
            model = self.mapper.to_model(game)
            session.merge(model)
            session.commit()
        finally:
            session.close()
    
    def get(self, game_id):
        session = self.session_factory()
        try:
            model = session.query(self.mapper.model_class).filter_by(id=game_id).first()
            return self.mapper.to_domain(model) if model else None
        finally:
            session.close()
    
    def get_all_waiting(self):
        session = self.session_factory()
        try:
            models = session.query(self.mapper.model_class).filter_by(state='waiting').all()
            return [self.mapper.to_domain(m) for m in models]
        finally:
            session.close()