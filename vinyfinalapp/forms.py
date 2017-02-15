from django import forms
from .models import vinyusers

	
class LoginForm(forms.Form):
	
	User = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your user-id',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		}
	)
	
	
	Password = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		}
	)	

class RegForm(forms.Form):
	
	UserId = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your user-id',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		}
	)	
	Password = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		}
	)	
	Repeatpassword = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		}
	)	

class NewAccForm(forms.Form):
	
	FirstName = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your user-id',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		},
		initial= 'Vineet'
	)	
	LastName = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		},
		initial= 'Pattnaik'
	)	
	Email = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		},
		initial= 'Viny3645@gmail.com'
	)	
	Phone = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your user-id',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		},
		initial= '+8615000326539'
	)	
	Address1 = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		},
		initial= 'Room-101, Building-6'
	)	
	Address2 = forms.CharField(
		#widget=forms.Textarea,
		initial= 'Lane-32, Guangshun Rd'
	)
	City = forms.CharField(
		#widget=forms.Textarea,
		initial= 'Shanghai'
	)	
	State = forms.CharField(
		#widget=forms.Textarea,
		initial= 'ChangNing'
	)	
	Zip = forms.CharField(
		#widget=forms.Textarea,
		initial= '200335'
	)	
	Country = forms.CharField(
		#widget=forms.Textarea,
		initial= 'China'
	)

class ProfileForm(forms.Form):
	
	Languages = forms.ChoiceField(
	widget = forms.Select,
	choices=(('English', 'English'),('Hindi', 'Hindi'),('German','German'),('Chinese','Chinese'),('Japanese','Japanese')))
	
	FavouriteCategory = forms.ChoiceField(
	widget = forms.Select,
	choices=(('Birds','Birds'), ('Cats','Cats'), ('Dogs','Dogs'), ('Fish','Fish'), ('Reptiles','Reptiles')))
	
	Enable_Mylist = forms.BooleanField()
	Enable_Mybanner = forms.BooleanField()
	
class CategoryForm(forms.Form):
	
	CategoryId = forms.CharField(
		#widget=forms.Textarea,
	)
	
	CategoryName = forms.CharField(
		#widget=forms.Textarea,
	)	

class QuantityForm(forms.Form):
	
	quantity = forms.IntegerField( initial=1
		#widget=forms.Textarea,
	)  # label=('Quantity'),   Add this to have a label name for this field in the template
	
