from django.shortcuts import render

from django.shortcuts import render


def dashboard_view(request):
    # Example hardcoded data for actual wait times
    actual_wait_times = {
        'urgent': [30, 45, 50, 60, 40],
        'non_urgent': [60, 70, 80, 90, 75]
    }


    # Calculate average wait times
    avg_actual_urgent = sum(actual_wait_times['urgent']) / len(actual_wait_times['urgent'])
    avg_actual_non_urgent = sum(actual_wait_times['non_urgent']) / len(actual_wait_times['non_urgent'])

    context = {
        'avg_actual_urgent': avg_actual_urgent,
        'avg_actual_non_urgent': avg_actual_non_urgent,
    }
    return render(request, 'dashboard/dashboard.html', context)
