
# Register your models here.
from django.contrib import admin
from .models import Religion
from .models import Arti
from .models import Mantra
from .models import Hits
from .models import Post

class ReligionModelAdmin(admin.ModelAdmin):
		list_display = ["__str__", "religionName", "religionID", "religionHistory"]
		list_editable = ["religionName", "religionHistory"]
		search_fields = ["religionName", "religionID"]
		class Meta:
			model = Religion

class ArtiModelAdmin(admin.ModelAdmin):
		list_display = ["__str__", "artiName", "artiID", "artiText"]
		list_editable = ["artiName", "artiText"]
		search_fields = ["artiName", "artiID"]
		class Meta:
			model = Arti

class MantraModelAdmin(admin.ModelAdmin):
		list_display = ["__str__", "mantraName", "mantraID", "mantraText"]
		list_editable = ["mantraName", "mantraText"]
		search_fields = ["mantraName", "mantraID"]
		class Meta:
			model = Mantra

class HitsModelAdmin(admin.ModelAdmin):
		list_display = ["__str__", "contentID"]
		#list_editable = ["contentID",]
		search_fields = ["contentID"]
		class Meta:
			model = Hits

class PostModelAdmin(admin.ModelAdmin):
		list_display = ["__str__", "title", "updates", "timestamp"]
		list_display_links = ["updates"]
		list_editable = ["title"]
		list_filter = ["updates", "timestamp"]
		search_fields = ["title", "content"]		
		class Meta:
			model = Post

admin.site.register(Religion, ReligionModelAdmin)
admin.site.register(Arti, ArtiModelAdmin)
admin.site.register(Mantra, MantraModelAdmin)
admin.site.register(Hits, HitsModelAdmin)
admin.site.register(Post, PostModelAdmin)
# Register your models her
