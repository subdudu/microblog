from django.core.serializers.json import Serializer
from django.utils.encoding import smart_unicode



class AjaxSerializer(Serializer):
	'''serialize model to a simpler json string than django default
	'''

	def start_object(self, obj):
		self._current = {"pk": smart_unicode(obj._get_pk_val(), strings_only=True)}

	def end_object(self, obj):
		self.objects.append(self._current)
		self._current = None



