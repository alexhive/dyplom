# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Announce(models.Model):
    announce_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    announce_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    doc_name = models.CharField(max_length=512, blank=True)
    is_to_publish = models.SmallIntegerField(null=True, blank=True)
    user_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    code = models.CharField(max_length=64, blank=True)
    signer = models.CharField(max_length=1024, blank=True)
    number_field = models.CharField(max_length=32, db_column='number_', blank=True) # Field renamed because it ended with '_'.
    is_external = models.SmallIntegerField(null=True, blank=True)
    external_bulletin = models.CharField(max_length=1024, blank=True)
    external_number = models.CharField(max_length=512, blank=True)
    bulletin_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    unumber = models.CharField(max_length=256, blank=True)
    who_created = models.CharField(max_length=256, blank=True)
    who_modified = models.CharField(max_length=256, blank=True)
    who_submitted = models.CharField(max_length=4000, blank=True)
    info_for_operator = models.CharField(max_length=4000, blank=True)
    numeration_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    version = models.SmallIntegerField(null=True, blank=True)
    mod_reason = models.CharField(max_length=1024, blank=True)
    accantum_log_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    storage_log_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    announce_date = models.DateField(null=True, blank=True)
    dt_modify = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'announce'

class AuctionType(models.Model):
    auction_type_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    name = models.CharField(max_length=512, blank=True)
    left_shift = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    right_shift = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    is_public = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    workflow_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    is_oblig_add_info = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    add_info_len = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    is_frame = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    x_procedure = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'auction_type'

class Branch(models.Model):
    branch_id = models.DecimalField(max_digits=38, decimal_places=0)
    name = models.CharField(max_length=512, blank=True)
    sname = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = 'branch'

class Bulletin(models.Model):
    bulletin_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    name = models.CharField(max_length=32, blank=True)
    dt_publicat = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=1024, blank=True)
    is_published = models.SmallIntegerField(null=True, blank=True)
    is_published_preliminary = models.SmallIntegerField(null=True, blank=True)
    numeration_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    bulletin_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    max_announces = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    use_accept_schedule = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    is_state_change_allowed = models.SmallIntegerField(null=True, blank=True)
    bulletin_kind_id = models.FloatField(null=True, blank=True)
    dt_create = models.DateField(null=True, blank=True)
    dt_publicat_str = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'bulletin'

class Document(models.Model):
    doc_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    announce_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    doc_name = models.CharField(max_length=512, blank=True)
    file_name = models.CharField(max_length=256, blank=True)
    mime = models.CharField(max_length=1024, blank=True)
    doc_size = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    disc = models.CharField(max_length=10, blank=True)
    doc_accantum_id = models.CharField(max_length=36, blank=True)
    class Meta:
        db_table = 'document'

class DocumentType(models.Model):
    doc_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    name = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = 'document_type'

class Lot(models.Model):
    lot_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    purchase = models.ForeignKey('Purchase', null=True, blank=True)
    result_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    disc = models.CharField(max_length=2, blank=True)
    goods_quan = models.CharField(max_length=3000, blank=True)
    goods_place = models.CharField(max_length=3000, blank=True)
    goods_term = models.CharField(max_length=1024, blank=True)
    is_guarantee_required = models.SmallIntegerField(null=True, blank=True)
    guarantee_method = models.CharField(max_length=512, blank=True)
    guarantee = models.FloatField(null=True, blank=True)
    dt_deadline = models.DateField(null=True, blank=True)
    dt_open = models.DateField(null=True, blank=True)
    cancel_not_text = models.CharField(max_length=2048, blank=True)
    not_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    cancel_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    dt_cancel_not = models.DateField(null=True, blank=True)
    dt_accept = models.DateField(null=True, blank=True)
    qualif_requirements = models.CharField(max_length=1024, blank=True)
    additional_info = models.CharField(max_length=1024, blank=True)
    lot_description = models.CharField(max_length=2048, blank=True)
    lot_cost = models.FloatField(null=True, blank=True)
    is_lot_guarantee = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    guarantee_string = models.CharField(max_length=512, blank=True)
    upd_goods_quan = models.CharField(max_length=1024, blank=True)
    upd_goods_term = models.CharField(max_length=512, blank=True)
    upd_lot_description = models.CharField(max_length=2048, blank=True)
    lot_cost_curr_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    lot_num = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    guarantee_condition = models.CharField(max_length=1024, blank=True)
    guarantee_term = models.CharField(max_length=512, blank=True)
    guarantee_method_en = models.CharField(max_length=512, blank=True)
    guarantee_en = models.FloatField(null=True, blank=True)
    guarantee_string_en = models.CharField(max_length=512, blank=True)
    guarantee_condition_en = models.CharField(max_length=1024, blank=True)
    guarantee_term_en = models.CharField(max_length=512, blank=True)
    goods_quan_en = models.CharField(max_length=2048, blank=True)
    lot_description_en = models.CharField(max_length=2048, blank=True)
    goods_place_en = models.CharField(max_length=3072, blank=True)
    goods_term_en = models.CharField(max_length=1024, blank=True)
    dt_open_new = models.DateField(null=True, blank=True)
    prop_upd_string = models.CharField(max_length=200, blank=True)
    dt_deadline_new = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'lot'

class LotAssociation(models.Model):
    lot_assoc_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    lot_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    purchase_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    announce_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    upd_lot_description = models.CharField(max_length=2048, blank=True)
    upd_goods_quan = models.CharField(max_length=1024, blank=True)
    upd_goods_term = models.CharField(max_length=512, blank=True)
    upd_goods_place = models.CharField(max_length=2048, blank=True)
    upd_lot_description_en = models.CharField(max_length=2048, blank=True)
    upd_goods_quan_en = models.CharField(max_length=1024, blank=True)
    upd_goods_term_en = models.CharField(max_length=512, blank=True)
    upd_goods_place_en = models.CharField(max_length=2048, blank=True)
    prop_upd_string = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'lot_association'

class Purchase(models.Model):
    purchase_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    user = models.ForeignKey('Userdata', null=True, blank=True)
    auction_type = models.ForeignKey(AuctionType, null=True, blank=True)
    branch = models.ForeignKey(Branch, null=True, blank=True)
    announce_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    disc = models.CharField(max_length=2, blank=True)
    cost_dispatcher_code = models.CharField(max_length=512, blank=True)
    cost_dispatcher_name = models.CharField(max_length=1024, blank=True)
    cost_source = models.CharField(max_length=512, blank=True)
    purchase_cost = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=2048, blank=True)
    goods_name = models.CharField(max_length=4000, blank=True)
    goods_quan = models.CharField(max_length=3000, blank=True)
    doc_getting_place = models.CharField(max_length=512, blank=True)
    doc_getting_method = models.CharField(max_length=512, blank=True)
    present_place = models.CharField(max_length=512, blank=True)
    present_method = models.CharField(max_length=512, blank=True)
    open_place = models.CharField(max_length=512, blank=True)
    additional_info = models.CharField(max_length=4000, blank=True)
    start_bulletin_number = models.CharField(max_length=1024, blank=True)
    lot_count = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    start_number = models.CharField(max_length=512, blank=True)
    purchase_cost_curr_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    is_public = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    goods_name_full_clob = models.TextField(blank=True)
    goods_name_full_text = models.CharField(max_length=4000, blank=True)
    subject_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    form_version = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    doc_getting_place_en = models.CharField(max_length=512, blank=True)
    doc_getting_method_en = models.CharField(max_length=512, blank=True)
    present_place_en = models.CharField(max_length=512, blank=True)
    present_method_en = models.CharField(max_length=512, blank=True)
    open_place_en = models.CharField(max_length=1024, blank=True)
    goods_name_en = models.CharField(max_length=4000, blank=True)
    goods_quan_en = models.CharField(max_length=3000, blank=True)
    address_en = models.CharField(max_length=2048, blank=True)
    prop_upd_string = models.CharField(max_length=150, blank=True)
    frame_term = models.CharField(max_length=500, blank=True)
    frame_condition_purchase = models.CharField(max_length=4000, blank=True)
    frame_condition_select = models.CharField(max_length=4000, blank=True)
    frame_is_customer_general = models.SmallIntegerField(null=True, blank=True)
    frame_condition_one = models.CharField(max_length=4000, blank=True)
    is_frame_purchase = models.SmallIntegerField(null=True, blank=True)
    frame_participant_count = models.CharField(max_length=100, blank=True)
    purchase_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    frame_participant_count_en = models.CharField(max_length=500, blank=True)
    frame_condition_purchase_en = models.CharField(max_length=4000, blank=True)
    frame_condition_select_en = models.CharField(max_length=4000, blank=True)
    frame_condition_one_en = models.CharField(max_length=4000, blank=True)
    frame_term_en = models.CharField(max_length=500, blank=True)
    is_inter_announce_required = models.SmallIntegerField(null=True, blank=True)
    contract_end_term_str = models.CharField(max_length=255, blank=True)
    purchase_publicated = models.DateField(null=True, blank=True)
    user_name = models.TextField(blank=True)
    class Meta:
        db_table = 'purchase'

class PurchaseAnnounce(models.Model):
    announce_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    purchase_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    dt_protocol_str = models.CharField(max_length=255, blank=True)
    upd_goods_name = models.CharField(max_length=4000, blank=True)
    upd_goods_quan = models.CharField(max_length=3000, blank=True)
    upd_goods_term = models.CharField(max_length=1024, blank=True)
    upd_purchase_cost = models.FloatField(null=True, blank=True)
    dt_accept_for_winned_results_str = models.CharField(max_length=255, blank=True)
    lots = models.CharField(max_length=4000, blank=True)
    sum_result_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    upd_purchase_cost_curr_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    goods_name_full_clob = models.TextField(blank=True)
    goods_name_full_text = models.CharField(max_length=4000, blank=True)
    participants_info = models.TextField(blank=True)
    validity_term = models.CharField(max_length=1024, blank=True)
    additional_requirements = models.CharField(max_length=4000, blank=True)
    upd_goods_place = models.CharField(max_length=3000, blank=True)
    additional_info = models.TextField(blank=True)
    goods_code = models.CharField(max_length=256, blank=True)
    webportal_address = models.CharField(max_length=1024, blank=True)
    website_address = models.CharField(max_length=1024, blank=True)
    registration_account = models.CharField(max_length=1024, blank=True)
    participant_name = models.CharField(max_length=1000, blank=True)
    participant_address = models.CharField(max_length=1000, blank=True)
    participant_phone = models.CharField(max_length=1000, blank=True)
    proposal_price = models.FloatField(null=True, blank=True)
    international_start_ref = models.CharField(max_length=1024, blank=True)
    accept_ref = models.CharField(max_length=1024, blank=True)
    description_subject = models.CharField(max_length=4000, blank=True)
    proposal_price_curr_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    participant_fax = models.CharField(max_length=1000, blank=True)
    participant_email = models.CharField(max_length=200, blank=True)
    contract_conditions = models.TextField(blank=True)
    upd_address = models.CharField(max_length=2048, blank=True)
    dt_send_invitation_str = models.CharField(max_length=255, blank=True)
    grounds = models.CharField(max_length=1024, blank=True)
    isrefused = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    agreement_lots = models.CharField(max_length=1024, blank=True)
    agreement_issue_date_str = models.CharField(max_length=255, blank=True)
    reg_letter_number = models.CharField(max_length=1024, blank=True)
    letter_adoption_date_str = models.CharField(max_length=255, blank=True)
    reg_agreement_number = models.CharField(max_length=1024, blank=True)
    appellant = models.CharField(max_length=4000, blank=True)
    decision_number = models.CharField(max_length=256, blank=True)
    dt_decision_str = models.CharField(max_length=255, blank=True)
    decision = models.TextField(blank=True)
    commission_establish = models.TextField(blank=True)
    commission_decide = models.TextField(blank=True)
    classifier_goods_name = models.CharField(max_length=4000, blank=True)
    goods_code_en = models.CharField(max_length=256, blank=True)
    pages_amount = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    instance_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    accantum_announce_id = models.CharField(max_length=36, blank=True)
    is_saved_in_swh = models.SmallIntegerField(null=True, blank=True)
    is_saved_in_accantum = models.SmallIntegerField(null=True, blank=True)
    cancel_publication_who = models.CharField(max_length=20, blank=True)
    cancel_publication_dt_str = models.CharField(max_length=255, blank=True)
    cancel_publication_reason = models.CharField(max_length=2000, blank=True)
    is_publication_cancelled = models.FloatField(null=True, blank=True)
    classifier_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    prop_upd_string = models.CharField(max_length=150, blank=True)
    frame_number = models.CharField(max_length=500, blank=True)
    frame_contract_date_str = models.CharField(max_length=255, blank=True)
    frame_unit_one_cost = models.CharField(max_length=3000, blank=True)
    frame_term = models.CharField(max_length=500, blank=True)
    frame_condition_purchase_upd = models.CharField(max_length=4000, blank=True)
    frame_condition_select_upd = models.CharField(max_length=4000, blank=True)
    frame_condition_one_upd = models.CharField(max_length=4000, blank=True)
    frame_participant_count_upd = models.CharField(max_length=100, blank=True)
    report_symbols_count = models.FloatField(null=True, blank=True)
    is_verify_queue_required = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    u_application_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    c_application_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    contract_end_term = models.DateField(null=True, blank=True)
    contract_end_term_str = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'purchase_announce'

class Result(models.Model):
    result_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    cancel_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    not_type_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    result_type = models.ForeignKey('ResultType', null=True, blank=True)
    purchase = models.ForeignKey(Purchase, null=True, blank=True)
    announce_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    disc = models.CharField(max_length=10, blank=True)
    additional_info = models.CharField(max_length=2048, blank=True)
    cancel_not_text = models.CharField(max_length=2048, blank=True)
    dt_cancel_not = models.DateField(null=True, blank=True)
    dt_accept = models.DateField(null=True, blank=True)
    lots = models.CharField(max_length=4000, blank=True)
    additional_info_en = models.CharField(max_length=4000, blank=True)
    cancel_not_text_en = models.CharField(max_length=2048, blank=True)
    prop_upd_string = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'result'

class ResultType(models.Model):
    result_type_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    name = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = 'result_type'

class Userdata(models.Model):
    user_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=38)
    region_id = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    state_reg_code = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=512, blank=True)
    address = models.CharField(max_length=512, blank=True)
    phone = models.CharField(max_length=256, blank=True)
    fax = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=256, blank=True)
    person = models.CharField(max_length=512, blank=True)
    user_disc = models.CharField(max_length=10, blank=True)
    has_internet_account = models.SmallIntegerField(null=True, blank=True)
    who_created = models.CharField(max_length=256, blank=True)
    who_modified = models.CharField(max_length=256, blank=True)
    dt_modify = models.DateField(null=True, blank=True)
    dt_create = models.DateField(null=True, blank=True)
    dt_internet = models.DateField(null=True, blank=True)
    who_internet = models.CharField(max_length=256, blank=True)
    name_en = models.CharField(max_length=512, blank=True)
    address_en = models.CharField(max_length=512, blank=True)
    user_customer = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    post = models.CharField(max_length=256, blank=True)
    version = models.BigIntegerField(null=True, blank=True)
    is_contract_report_enabled = models.DecimalField(null=True, max_digits=38, decimal_places=0, blank=True)
    prop_upd_string = models.CharField(max_length=50, blank=True)
    type_id = models.FloatField(null=True, blank=True)
    father_name = models.CharField(max_length=512, blank=True)
    position = models.CharField(max_length=1000, blank=True)
    nick_name = models.CharField(max_length=1000, blank=True)
    is_active = models.SmallIntegerField(null=True, blank=True)
    is_organisation_active = models.SmallIntegerField(null=True, blank=True)
    office = models.CharField(max_length=100, blank=True)
    is_admin = models.SmallIntegerField(null=True, blank=True)
    additional_services = models.SmallIntegerField(null=True, blank=True)
    literal = models.CharField(max_length=1, blank=True)
    principal = models.CharField(max_length=250, blank=True)
    correspondence_address = models.CharField(max_length=250, blank=True)
    uses_digital_signature = models.SmallIntegerField(null=True, blank=True)
    sur_name = models.CharField(max_length=250, blank=True)
    second_name = models.CharField(max_length=250, blank=True)
    is_chief = models.SmallIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = 'userdata'

class UserdataSort(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    parent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=512, blank=True)
    class Meta:
        db_table = 'userdata_sort'

class W(models.Model):
    w_id = models.IntegerField(primary_key=True)
    w_name = models.TextField(unique=True, blank=True)
    class Meta:
        db_table = 'w'

class Winner(models.Model):
    winner_id = models.DecimalField(primary_key=True,unique=True, max_digits=38, decimal_places=0)
    purchase = models.ForeignKey(Purchase, null=True, blank=True)
    announce = models.ForeignKey(Announce, null=True, blank=True)
    winner_name = models.CharField(max_length=1024, blank=True)
    winner_code = models.CharField(max_length=64, blank=True)
    winner_address = models.CharField(max_length=1024, blank=True)
    winner_phone = models.CharField(max_length=1024, blank=True)
    winner_address_full = models.CharField(max_length=2048, blank=True)
    winner_name_en = models.CharField(max_length=1024, blank=True)
    winner_address_en = models.CharField(max_length=1024, blank=True)
    winner_address_full_en = models.CharField(max_length=2048, blank=True)
    prop_upd_string = models.CharField(max_length=100, blank=True)
    w_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'winner'

class WinnerPurchaseMapping(models.Model):
    winner_name = models.TextField()
    winner_code = models.CharField(max_length=255, blank=True)
    w_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'winner_purchase_mapping'

class WinnerSort(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    parent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=1024, blank=True)
    class Meta:
        db_table = 'winner_sort'

