from django.shortcuts import render
from django.views import View

from lookapp.models import Category


# Create your views here.

class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        rows = []

        for parent in categories.filter(level=0):
            parent_name = parent.name
            first_parent_row = True

            children = parent.get_children()
            if children.exists():
                for child in children:
                    child_name = child.name
                    first_child_row = True

                    grandchildren = child.get_children()
                    if grandchildren.exists():
                        for grandchild in grandchildren:
                            rows.append({
                                'parent': parent_name if first_parent_row else '',
                                'child': child_name if first_child_row else '',
                                'grandchild': grandchild.name
                            })
                            first_parent_row = False
                            first_child_row = False
                    else:
                        rows.append({
                            'parent': parent_name if first_parent_row else '',
                            'child': child_name if first_child_row else '',
                            'grandchild': ''
                        })
                        first_parent_row = False
                        first_child_row = False
            else:
                rows.append({
                    'parent': parent_name,
                    'child': '',
                    'grandchild': ''
                })
        return render(request, 'base.html', context={'rows': rows})

