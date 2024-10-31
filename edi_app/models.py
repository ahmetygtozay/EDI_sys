from django.db import models

from django.db import models

# edi_app/models.py
from django.db import models

from django.db import models

class EDIMessage(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('ORDER', 'Order'),
        ('INVOICE', 'Invoice'),
        ('SHIPMENT', 'Shipment'),
    ]

    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    document_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES) 
    document_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.document_type} from {self.sender} to {self.receiver}"

    class Meta:
        ordering = ['created_at']  

# edi_app/models.py
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)        
    email = models.EmailField(unique=True)            
    phone = models.CharField(max_length=20, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True) 
    supplier_name = models.CharField(max_length=255)   
    supplier_code = models.CharField(max_length=50, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)     
    product_code = models.CharField(max_length=50, unique=True)  
    product_name = models.CharField(max_length=255)     
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.product_name
# edi_translator.py

# edi_translator.py

class EDITranslator:
    def __init__(self):
        self.segment_definitions = {
            'UNH': 'Message Header',
            'BGM': 'Beginning of Message',
            'DTM': 'Date/Time/Period',
            'NAD': 'Name and Address',
            'LIN': 'Line Item',
            'QTY': 'Quantity',
            'PRI': 'Price',
            'UNS': 'Section Control',
            'CNT': 'Control Total',
            'UNT': 'End of Message',
            'UNZ': 'Interchange Control'
        }

    def parse_segment(self, segment_code, segment_content):
        parsed_content = ""
        
        if segment_code == 'UNH':
            parsed_content = f"Message Type: {segment_content[1] if len(segment_content) > 1 else ''}, Reference Number: {segment_content[0] if segment_content else ''}"

        elif segment_code == 'BGM':
            parsed_content = f"Message Type: {segment_content[0] if segment_content else ''}, Document Number: {segment_content[1] if len(segment_content) > 1 else ''}, Message Function: {segment_content[2] if len(segment_content) > 2 else ''}"

        elif segment_code == 'DTM':
            parsed_content = f"Date/Time/Period Code: {segment_content[0] if segment_content else ''}, Date/Time: {segment_content[1] if len(segment_content) > 1 else ''}, Format: {segment_content[2] if len(segment_content) > 2 else ''}"

        elif segment_code == 'NAD':
            parsed_content = f"Party Qualifier: {segment_content[0] if segment_content else ''}, Party ID: {segment_content[1] if len(segment_content) > 1 else ''}"

        elif segment_code == 'LIN':
            parsed_content = f"Line Item Number: {segment_content[0] if segment_content else ''}, Product ID: {segment_content[2] if len(segment_content) > 2 else ''}"

        elif segment_code == 'QTY':
            parsed_content = f"Quantity Type: {segment_content[0] if segment_content else ''}, Quantity: {segment_content[1] if len(segment_content) > 1 else ''}"

        elif segment_code == 'PRI':
            parsed_content = f"Price Qualifier: {segment_content[0] if segment_content else ''}, Price: {segment_content[1] if len(segment_content) > 1 else ''}"

        elif segment_code == 'UNS':
            parsed_content = f"Section Identification: {segment_content[0] if segment_content else ''}"

        elif segment_code == 'CNT':
            parsed_content = f"Control Qualifier: {segment_content[0] if segment_content else ''}, Control Value: {segment_content[1] if len(segment_content) > 1 else ''}"

        elif segment_code == 'UNT':
            parsed_content = f"Number of Segments: {segment_content[0] if segment_content else ''}, Message Reference Number: {segment_content[1] if len(segment_content) > 1 else ''}"

        elif segment_code == 'UNZ':
            parsed_content = f"Interchange Control Count: {segment_content[0] if segment_content else ''}, Interchange Control Reference: {segment_content[1] if len(segment_content) > 1 else ''}"

        else:
            parsed_content = "Unknown Segment Details"

        return parsed_content

    def translate(self, edi_message):
        translated_segments = []
        segments = edi_message.split("'") 

        for segment in segments:
            segment = segment.strip() 
            if not segment:
                continue  

            segment_parts = segment.split('+')  
            segment_code = segment_parts[0]   
            segment_content = segment_parts[1:]  

            if segment_code in self.segment_definitions:
                segment_description = f"{self.segment_definitions[segment_code]} -> {segment}"
                parsed_content = self.parse_segment(segment_code, segment_content)
                translated_segments.append(f"{segment_description}\n    {parsed_content}")
            else:
                translated_segments.append(f"Unrecognized Segment: {segment}")

        return "\n".join(translated_segments)
