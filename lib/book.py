class Book:
    def __init__(self, title, page_count, publication_year):
        self.title = title
        self.page_count = page_count  # Add page_count attribute
        self.publication_year = publication_year
        self.checked_out = False

    def checkout(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False

    def checkin(self):
        if self.checked_out:
            self.checked_out = False
            return True
        else:
            return False
