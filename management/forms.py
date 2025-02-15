from django import forms
from .models import *
# Order, OrderItem, Supplier, Bengkel, Product, Stock, Brand, Category, Penawaran

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['bukti']


class PenawaranForm(forms.ModelForm):
    class Meta:
        model = Penawaran
        fields = ['tujuan','deskripsi']
        widgets = {
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'tujuan': forms.Select(attrs={'class': 'form-control'}),
        }

class TransaksiBaru(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier','bengkel']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'bengkel': forms.Select(attrs={'class': 'form-control'}),
        }

class TransaksiItem(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        fields = ['quantity','product']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }
    

# class TransaksiItem(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['quantity','product']
#         widgets = {
#         'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#         'product': forms.Select(attrs={'class': 'form-control'}),
        # }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','image','brand','category']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
            'brand' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.CheckboxSelectMultiple(),
        }

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','image','category']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
            'brand' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.CheckboxSelectMultiple(),
        }



