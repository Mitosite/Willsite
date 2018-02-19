from django import forms



class UploadFileForm(forms.Form):
	title = forms.CharField(label='Your name', max_length=100)
	file = forms.FileField()
	user_email = forms.EmailField(required=False)

class SingleJobForm(forms.Form):
	#form to submit single job
	readsfile = forms.FileField(label='Reads file:')
	#adapters = forms.CharField(label='Adapter sequence:', max_length=50)
	#key = forms.CharField(label='Random key:', max_length=10)
	user_email = forms.EmailField(required=False)

class PairedJobForm(forms.Form):
	readsfile1 = forms.FileField(label='First reads file:')
	readsfile2 = forms.FileField(label='Second reads file:')
	adapters = forms.CharField(label='Adapter sequence:', max_length=50)
	key = forms.CharField(label='Random key:', max_length=10)


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
