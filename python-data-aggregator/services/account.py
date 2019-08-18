from services.base import Base


class Account(Base):
    def get_data(self):
        return self.get("/")

    def get_account(self, ac_id):
        return [el for el in self.get_data() if el["id"] == ac_id][0]
