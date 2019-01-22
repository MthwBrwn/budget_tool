from django.urls import path
from .views import BudgetView, TransactionView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('budget', BudgetView.as_view(), name='budget_view'),
    path('transaction/<int:id>', TransactionView.as_view(), name='transaction_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
