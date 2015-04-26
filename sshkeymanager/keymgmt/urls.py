from django.conf.urls import patterns, url

from keymgmt.views import (
    HomeView,
    EnvironmentList,
    EnvironmentCreate,
    EnvironmentDelete,
    EnvironmentDetail,
    EnvironmentUpdate,
    SSHKeyList,
    SSHKeyCreate,
    SSHKeyUpdate,
    SSHKeyDelete,
    SSHKeyDetail,
    GroupList,
    GroupCreate,
    GroupDelete,
    GroupDetail,
    HostList,
    HostCreate,
    HostDetail,
    HostDelete,
    SSHKeyringList,
    SSHKeyringCreate,
    SSHKeyringUpdate,
    SSHKeyringDelete,
    SSHKeyringDetail,
    SSHAccountList,
    SSHAccountDetail,
    SSHAccountCreateEnvironment,
    SSHAccountCreateHost,
    SSHAccountCreateGroup,
    SSHAccountUpdate,
    SSHAccountDelete,
    SSHAccountKeyUpdate,
    SSHAccountAvailableList,
    SSHAccountAvailableDelete,
    GroupRuleCreate,
    GroupRuleDelete,
    GroupRuleUpdate,
    AuditKey2Access,
    api_get_keys,
)

urlpatterns = patterns('',
    url(r'^environment/$', EnvironmentList.as_view(), name='environment_list'),
    url(r'^environment/add/$', EnvironmentCreate.as_view(), name='environment_create'),
    url(r'^environment/(?P<pk>[0-9]+)/delete/$', EnvironmentDelete.as_view(), name='environment_delete'),
    url(r'^environment/(?P<pk>[0-9]+)/update/$', EnvironmentUpdate.as_view(), name='environment_update'),
    url(r'^environment/(?P<pk>[0-9]+)/$', EnvironmentDetail.as_view(), name='environment_detail'),

    url(r'^sshkey/$', SSHKeyList.as_view(), name='sshkey_list'),
    url(r'^sshkey/add/$', SSHKeyCreate.as_view(), name='sshkey_create'),
    url(r'^sshkey/(?P<pk>[0-9]+)/delete/$', SSHKeyDelete.as_view(), name='sshkey_delete'),
    url(r'^sshkey/(?P<pk>[0-9]+)/update/$', SSHKeyUpdate.as_view(), name='sshkey_update'),
    url(r'^sshkey/(?P<pk>[0-9]+)/$', SSHKeyDetail.as_view(), name='sshkey_detail'),

    url(r'^group/$', GroupList.as_view(), name='group_list'),
    url(r'^group/add/$', GroupCreate.as_view(), name='group_create'),
    url(r'^group/(?P<pk>[0-9]+)/delete/$', GroupDelete.as_view(), name='group_delete'),
    url(r'^group/(?P<pk>[0-9]+)/$', GroupDetail.as_view(), name='group_detail'),

    url(r'^group/(?P<pk>[0-9]+)/rule/add/$', GroupRuleCreate.as_view(), name='group_rule_create'),
    url(r'^group/(?P<group_pk>[0-9]+)/rule/(?P<pk>[0-9]+)/delete/$', GroupRuleDelete.as_view(), name='group_rule_delete'),
    url(r'^group/(?P<group_pk>[0-9]+)/rule/(?P<pk>[0-9]+)/update/$', GroupRuleUpdate.as_view(), name='group_rule_update'),

    url(r'^host/$', HostList.as_view(), name='host_list'),
    url(r'^host/add/$', HostCreate.as_view(), name='host_create'),
    url(r'^host/(?P<pk>[0-9]+)/$', HostDetail.as_view(), name='host_detail'),
    url(r'^host/(?P<pk>[0-9]+)/delete/$', HostDelete.as_view(), name='host_delete'),

    url(r'^keyring/$', SSHKeyringList.as_view(), name='sshkeyring_list'),
    url(r'^keyring/add/$', SSHKeyringCreate.as_view(), name='sshkeyring_create'),
    url(r'^keyring/(?P<pk>[0-9]+)/$', SSHKeyringDetail.as_view(), name='sshkeyring_detail'),
    url(r'^keyring/(?P<pk>[0-9]+)/update/$', SSHKeyringUpdate.as_view(), name='sshkeyring_update'),
    url(r'^keyring/(?P<pk>[0-9]+)/delete/$', SSHKeyringDelete.as_view(), name='sshkeyring_delete'),

    url(r'^sshaccount/$', SSHAccountList.as_view(), name='sshaccount_list'),
    url(r'^sshaccount/(?P<pk>[0-9]+)/$', SSHAccountDetail.as_view(), name='sshaccount_detail'),
    url(r'^sshaccount/(?P<pk>[0-9]+)/delete/$', SSHAccountDelete.as_view(), name='sshaccount_delete'),
    url(r'^sshaccount/(?P<pk>[0-9]+)/update/$', SSHAccountUpdate.as_view(), name='sshaccount_update'),
    url(r'^sshaccount/(?P<pk>[0-9]+)/key/$', SSHAccountKeyUpdate.as_view(), name='sshaccount_key_update'),
    url(r'^sshaccount/add/environment$', SSHAccountCreateEnvironment.as_view(), name='sshaccount_create_environment'),
    url(r'^sshaccount/add/host$', SSHAccountCreateHost.as_view(), name='sshaccount_create_host'),
    url(r'^sshaccount/add/group$', SSHAccountCreateGroup.as_view(), name='sshaccount_create_group'),

    url(r'^sshaccountavailable/$', SSHAccountAvailableList.as_view(), name='sshaccountavailable_list'),
    url(r'^sshaccountavailable/(?P<pk>[0-9]+)/delete/$', SSHAccountAvailableDelete.as_view(), name='sshaccountavailable_delete'),

    url(r'^audit/key2access/$', AuditKey2Access.as_view(), name='audit_key2access'),

    url(r'^api/getkeys/$', api_get_keys),

    url(r'^$', HomeView.as_view(), name='home'),
)