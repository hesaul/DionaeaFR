import django_tables2 as tables
from django.utils.safestring import mark_safe
from Web.models import Download

class LinkID(tables.Column):
	def render(self, value):
		return mark_safe('<a href="/connections/' + str(value) + '">' + str(value) + '</a>')

class DownloadsTable(tables.Table):
	connection = LinkID()
	class Meta:
		model = Download
		exclude = ("download", )
		attrs = {"class": "bootstrap"}
		empty_text = 'No data.'
		template = 'tables/bootstrap.html'
