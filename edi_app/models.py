from django.db import models

from django.db import models

# edi_app/models.py
from django.db import models

class EDIMessage(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    document_type = models.CharField(max_length=255)
    document_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.document_type} from {self.sender} to {self.receiver}"

# edi_app/models.py
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Otomatik artan ID
    name = models.CharField(max_length=255)            # Müşteri adı
    email = models.EmailField(unique=True)              # Müşteri e-posta adresi
    phone = models.CharField(max_length=20, blank=True) # Müşteri telefon numarası
    created_at = models.DateTimeField(auto_now_add=True) # Kayıt tarihi

    def __str__(self):
        return self.name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)  # Otomatik artan ID
    supplier_name = models.CharField(max_length=255)   # Tedarikçi adı
    supplier_code = models.CharField(max_length=50, unique=True)  # Tedarikçi kodu
    created_at = models.DateTimeField(auto_now_add=True) # Kayıt tarihi

    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)     # Otomatik artan ID
    product_code = models.CharField(max_length=50, unique=True)  # Ürün kodu
    product_name = models.CharField(max_length=255)      # Ürün adı
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)  # Tedarikçi ilişkisi
    created_at = models.DateTimeField(auto_now_add=True)  # Kayıt tarihi

    def __str__(self):
        return self.product_name
