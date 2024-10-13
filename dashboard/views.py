from django.shortcuts import render


def dashboard_view(request):
    # Example hardcoded data for actual wait times
    actual_wait_times = {
        'urgent': [120, 450, 222, 160, 140],
        'routine': [300, 600, 400, 200, 250]
    }


    # Calculate average wait times
    avg_actual_urgent = sum(actual_wait_times['urgent']) / len(actual_wait_times['urgent'])
    avg_actual_routine = sum(actual_wait_times['routine']) / len(actual_wait_times['routine'])

    context = {
        'avg_actual_urgent': avg_actual_urgent,
        'avg_actual_routine': avg_actual_routine,
    }
    return render(request, 'dashboard/dashboard.html', context)
