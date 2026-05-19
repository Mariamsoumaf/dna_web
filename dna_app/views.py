from django.shortcuts import render
from .dna_logic import analyze_dna
from .models import DNAResult


def home(request):
    if request.method == 'POST':
        result = analyze_dna(request.POST.get('dna', ''))
        if result.get('error'):
            return render(request, 'dna_app/home.html', result)
        DNAResult.objects.create(
            sequence=result['sequence'], count_a=result['count_a'],
            count_t=result['count_t'], count_c=result['count_c'],
            count_g=result['count_g'], is_valid=result['valid'])
        return render(request, 'dna_app/result.html', {'result': result})
    return render(request, 'dna_app/home.html')


def history(request):
    return render(request, 'dna_app/history.html',
                  {'records': DNAResult.objects.all().order_by('-created_at')})
