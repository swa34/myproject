from django.shortcuts import render
import openai

openai.api_key = "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"


def index(request):
    if request.method == 'POST':
        question = request.POST['question']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.5,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return render(request, 'response.html', {'response': response.choices[0].text})
    else:
        return render(request, 'index.html')
