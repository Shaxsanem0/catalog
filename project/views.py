from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review, Category, Like
from django.contrib.auth.decorators import login_required

def home_view(request):
    query = request.GET.get('q', '')#query-поисковой запрос
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    context = {#формирование
        'products': products,
        'categories': categories,
        'query': query,
    }
    return render(request, 'home.html', context)


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            Review.objects.create(product=product, rating=rating, comment=comment)
            return redirect('product_detail', product_id=product.id)

    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)

def category_detail_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products=Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category_detail.html', context)

def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    products = Product.objects.all()

    # Текстовый поиск
    if query:
        products = products.filter(
            Q(nameicontains=query) | Q(category_contains=query)
        )

    # Фильтр по категории
    if category_id:
        products = products.filter(category_id=category_id)

    # Фильтр по минимальной цене
    if min_price:
        products = products.filter(price__gte=min_price)

    # Фильтр по максимальной цене
    if max_price:
        products = products.filter(price__lte=max_price)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'store/product_list.html', context)


@login_required
def toggle_like(request, product_id): #request-запрос
    product = get_object_or_404(Product, id=product_id)
    like, created = Like.objects.get_or_create(user=request.user, product=product)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': product.likes.count()
    })