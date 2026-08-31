from datasource.mapper.user_mapper import UserMapper


class UserRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.mapper = UserMapper()
    
    def save(self, user):
        session = self.session_factory()
        try:
            model = self.mapper.to_model(user)
            session.merge(model)
            session.commit()
        finally:
            session.close()
    
    def get(self, user_id):
        session = self.session_factory()
        try:
            model = session.query(self.mapper.model_class).filter_by(id=user_id).first()
            return self.mapper.to_domain(model) if model else None
        finally:
            session.close()
    
    def get_by_login(self, login):
        session = self.session_factory()
        try:
            model = session.query(self.mapper.model_class).filter_by(login=login).first()
            return self.mapper.to_domain(model) if model else None
        finally:
            session.close()