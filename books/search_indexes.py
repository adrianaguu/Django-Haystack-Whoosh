from haystack import indexes
from .models import Book


class BookIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True, template_name="search/book_text.txt")
	title = indexes.CharField(model_attr='title')

	def get_model(self):
            return Book