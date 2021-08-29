from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Membership, Article, Tag


class MembershipInlineFormset(BaseInlineFormSet):
    def clean(self):
        primary_tags_count = 0

        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data.get('is_tag_primary', None):
                primary_tags_count += 1

        if primary_tags_count > 1:
            raise ValidationError('Основным может быть лишь один тэг!')

        return super().clean()


class MembershipInline(admin.TabularInline):
    model = Membership
    formset = MembershipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
