from django.contrib import admin
 
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notifications,Reciept,Loan,Reward
class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","email")
    search_fields=("first_name","last_name")


admin.site.register(Customer,CustomerAdmin) 
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notifications)
admin.site.register(Reciept)
admin.site.register(Loan)
admin.site.register(Reward)




