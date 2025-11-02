from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Mission)
class MissionTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


@register(MissionPoint)
class MissionPointTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Value)
class ValueTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


@register(Achievement)
class AchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


@register(Member)
class MemberTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'bio')


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


@register(ManufacturingOverview)
class ManufacturingOverviewTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ManufacturingStat)
class ManufacturingStatTranslationOptions(TranslationOptions):
    fields = ('label',)


@register(ProductionLine)
class ProductionLineTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(GalleryCategory)
class GalleryCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(PartnershipBenefit)
class PartnershipBenefitTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'usage', 'composition', 'badge', 'specs', 'country', 'certificates')


@register(ProductFeature)
class ProductFeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', )
