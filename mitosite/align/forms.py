from django import forms
from align.models import UploadFile, Pairedjob


class UploadFileForm(forms.Form):
	title = forms.CharField(label='Your name', max_length=100)
	#class Meta:
		#model = UploadFile
		#fields = ('title', 'file')

class PairedJobForm(forms.Form):
	readsfile1 = forms.FileField()


'''
class RetrieveJobForm(forms.Form):
	class Meta:
		model = RetrieveJob
		fields = ('userkey')

class SinglejobForm(forms.Form):
	class Meta:
		model = Singlejob
		fields = ('original_filename', 'sreads_file', 'user_email')


	def check_fastq(self):
								file = self.cleaned_data.get('file')
								if not file:
									raise forms.ValidationError('Please upload a valid file.')
								if not file.name.endswith('.fastq'):
									raise forms.ValidationError("Incorrect file format. Pease upload files ending in '.fasta'.")
								return super(UploadFileForm, self).check_fastq()'''
