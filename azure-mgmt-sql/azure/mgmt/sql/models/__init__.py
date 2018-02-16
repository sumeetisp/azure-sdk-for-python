# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource
from .proxy_resource import ProxyResource
from .backup_long_term_retention_policy import BackupLongTermRetentionPolicy
from .backup_long_term_retention_vault import BackupLongTermRetentionVault
from .tracked_resource import TrackedResource
from .restore_point import RestorePoint
from .recoverable_database import RecoverableDatabase
from .restorable_dropped_database import RestorableDroppedDatabase
from .max_size_capability import MaxSizeCapability
from .service_objective_capability import ServiceObjectiveCapability
from .edition_capability import EditionCapability
from .elastic_pool_per_database_min_dtu_capability import ElasticPoolPerDatabaseMinDtuCapability
from .elastic_pool_per_database_max_dtu_capability import ElasticPoolPerDatabaseMaxDtuCapability
from .elastic_pool_dtu_capability import ElasticPoolDtuCapability
from .elastic_pool_edition_capability import ElasticPoolEditionCapability
from .server_version_capability import ServerVersionCapability
from .location_capabilities import LocationCapabilities
from .check_name_availability_request import CheckNameAvailabilityRequest
from .check_name_availability_response import CheckNameAvailabilityResponse
from .server_connection_policy import ServerConnectionPolicy
from .slo_usage_metric import SloUsageMetric
from .service_tier_advisor import ServiceTierAdvisor
from .transparent_data_encryption import TransparentDataEncryption
from .operation_impact import OperationImpact
from .recommended_index import RecommendedIndex
from .database import Database
from .database_update import DatabaseUpdate
from .transparent_data_encryption_activity import TransparentDataEncryptionActivity
from .elastic_pool_database_activity import ElasticPoolDatabaseActivity
from .elastic_pool_activity import ElasticPoolActivity
from .recommended_elastic_pool_metric import RecommendedElasticPoolMetric
from .recommended_elastic_pool import RecommendedElasticPool
from .database_security_alert_policy import DatabaseSecurityAlertPolicy
from .data_masking_policy import DataMaskingPolicy
from .data_masking_rule import DataMaskingRule
from .elastic_pool import ElasticPool
from .elastic_pool_update import ElasticPoolUpdate
from .firewall_rule import FirewallRule
from .geo_backup_policy import GeoBackupPolicy
from .import_extension_request import ImportExtensionRequest
from .import_export_response import ImportExportResponse
from .import_request import ImportRequest
from .export_request import ExportRequest
from .metric_value import MetricValue
from .metric_name import MetricName
from .metric import Metric
from .metric_availability import MetricAvailability
from .metric_definition import MetricDefinition
from .replication_link import ReplicationLink
from .server_azure_ad_administrator import ServerAzureADAdministrator
from .server_communication_link import ServerCommunicationLink
from .service_objective import ServiceObjective
from .server_usage import ServerUsage
from .database_usage import DatabaseUsage
from .database_blob_auditing_policy import DatabaseBlobAuditingPolicy
from .automatic_tuning_options import AutomaticTuningOptions
from .database_automatic_tuning import DatabaseAutomaticTuning
from .encryption_protector import EncryptionProtector
from .failover_group_read_write_endpoint import FailoverGroupReadWriteEndpoint
from .failover_group_read_only_endpoint import FailoverGroupReadOnlyEndpoint
from .partner_info import PartnerInfo
from .failover_group import FailoverGroup
from .failover_group_update import FailoverGroupUpdate
from .operation_display import OperationDisplay
from .operation import Operation
from .server_key import ServerKey
from .resource_identity import ResourceIdentity
from .server import Server
from .server_update import ServerUpdate
from .sync_agent import SyncAgent
from .sync_agent_key_properties import SyncAgentKeyProperties
from .sync_agent_linked_database import SyncAgentLinkedDatabase
from .sync_database_id_properties import SyncDatabaseIdProperties
from .sync_full_schema_table_column import SyncFullSchemaTableColumn
from .sync_full_schema_table import SyncFullSchemaTable
from .sync_full_schema_properties import SyncFullSchemaProperties
from .sync_group_log_properties import SyncGroupLogProperties
from .sync_group_schema_table_column import SyncGroupSchemaTableColumn
from .sync_group_schema_table import SyncGroupSchemaTable
from .sync_group_schema import SyncGroupSchema
from .sync_group import SyncGroup
from .sync_member import SyncMember
from .subscription_usage import SubscriptionUsage
from .virtual_network_rule import VirtualNetworkRule
from .database_operation import DatabaseOperation
from .resource_move_definition import ResourceMoveDefinition
from .automatic_tuning_server_options import AutomaticTuningServerOptions
from .server_automatic_tuning import ServerAutomaticTuning
from .server_dns_alias import ServerDnsAlias
from .server_dns_alias_acquisition import ServerDnsAliasAcquisition
from .backup_long_term_retention_policy_paged import BackupLongTermRetentionPolicyPaged
from .backup_long_term_retention_vault_paged import BackupLongTermRetentionVaultPaged
from .restore_point_paged import RestorePointPaged
from .recoverable_database_paged import RecoverableDatabasePaged
from .restorable_dropped_database_paged import RestorableDroppedDatabasePaged
from .server_paged import ServerPaged
from .database_paged import DatabasePaged
from .metric_paged import MetricPaged
from .metric_definition_paged import MetricDefinitionPaged
from .data_masking_rule_paged import DataMaskingRulePaged
from .elastic_pool_paged import ElasticPoolPaged
from .firewall_rule_paged import FirewallRulePaged
from .geo_backup_policy_paged import GeoBackupPolicyPaged
from .replication_link_paged import ReplicationLinkPaged
from .server_azure_ad_administrator_paged import ServerAzureADAdministratorPaged
from .server_communication_link_paged import ServerCommunicationLinkPaged
from .service_objective_paged import ServiceObjectivePaged
from .elastic_pool_activity_paged import ElasticPoolActivityPaged
from .elastic_pool_database_activity_paged import ElasticPoolDatabaseActivityPaged
from .recommended_elastic_pool_paged import RecommendedElasticPoolPaged
from .recommended_elastic_pool_metric_paged import RecommendedElasticPoolMetricPaged
from .service_tier_advisor_paged import ServiceTierAdvisorPaged
from .transparent_data_encryption_activity_paged import TransparentDataEncryptionActivityPaged
from .server_usage_paged import ServerUsagePaged
from .database_usage_paged import DatabaseUsagePaged
from .encryption_protector_paged import EncryptionProtectorPaged
from .failover_group_paged import FailoverGroupPaged
from .operation_paged import OperationPaged
from .server_key_paged import ServerKeyPaged
from .sync_agent_paged import SyncAgentPaged
from .sync_agent_linked_database_paged import SyncAgentLinkedDatabasePaged
from .sync_database_id_properties_paged import SyncDatabaseIdPropertiesPaged
from .sync_full_schema_properties_paged import SyncFullSchemaPropertiesPaged
from .sync_group_log_properties_paged import SyncGroupLogPropertiesPaged
from .sync_group_paged import SyncGroupPaged
from .sync_member_paged import SyncMemberPaged
from .subscription_usage_paged import SubscriptionUsagePaged
from .virtual_network_rule_paged import VirtualNetworkRulePaged
from .database_operation_paged import DatabaseOperationPaged
from .server_dns_alias_paged import ServerDnsAliasPaged
from .sql_management_client_enums import (
    BackupLongTermRetentionPolicyState,
    RestorePointType,
    CapabilityStatus,
    MaxSizeUnits,
    PerformanceLevelUnit,
    CheckNameAvailabilityReason,
    ServerConnectionType,
    CreateMode,
    DatabaseEdition,
    ServiceObjectiveName,
    TransparentDataEncryptionStatus,
    RecommendedIndexAction,
    RecommendedIndexState,
    RecommendedIndexType,
    ReadScale,
    SampleName,
    TransparentDataEncryptionActivityStatus,
    ElasticPoolEdition,
    SecurityAlertPolicyState,
    SecurityAlertPolicyEmailAccountAdmins,
    SecurityAlertPolicyUseServerDefault,
    DataMaskingState,
    DataMaskingRuleState,
    DataMaskingFunction,
    ElasticPoolState,
    GeoBackupPolicyState,
    StorageKeyType,
    AuthenticationType,
    UnitType,
    PrimaryAggregationType,
    UnitDefinitionType,
    ReplicationRole,
    ReplicationState,
    BlobAuditingPolicyState,
    AutomaticTuningMode,
    AutomaticTuningOptionModeDesired,
    AutomaticTuningOptionModeActual,
    AutomaticTuningDisabledReason,
    ServerKeyType,
    ReadWriteEndpointFailoverPolicy,
    ReadOnlyEndpointFailoverPolicy,
    FailoverGroupReplicationRole,
    OperationOrigin,
    IdentityType,
    SyncAgentState,
    SyncMemberDbType,
    SyncGroupLogType,
    SyncConflictResolutionPolicy,
    SyncGroupState,
    SyncDirection,
    SyncMemberState,
    VirtualNetworkRuleState,
    ManagementOperationState,
    AutomaticTuningServerMode,
    AutomaticTuningServerReason,
)

__all__ = [
    'Resource',
    'ProxyResource',
    'BackupLongTermRetentionPolicy',
    'BackupLongTermRetentionVault',
    'TrackedResource',
    'RestorePoint',
    'RecoverableDatabase',
    'RestorableDroppedDatabase',
    'MaxSizeCapability',
    'ServiceObjectiveCapability',
    'EditionCapability',
    'ElasticPoolPerDatabaseMinDtuCapability',
    'ElasticPoolPerDatabaseMaxDtuCapability',
    'ElasticPoolDtuCapability',
    'ElasticPoolEditionCapability',
    'ServerVersionCapability',
    'LocationCapabilities',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'ServerConnectionPolicy',
    'SloUsageMetric',
    'ServiceTierAdvisor',
    'TransparentDataEncryption',
    'OperationImpact',
    'RecommendedIndex',
    'Database',
    'DatabaseUpdate',
    'TransparentDataEncryptionActivity',
    'ElasticPoolDatabaseActivity',
    'ElasticPoolActivity',
    'RecommendedElasticPoolMetric',
    'RecommendedElasticPool',
    'DatabaseSecurityAlertPolicy',
    'DataMaskingPolicy',
    'DataMaskingRule',
    'ElasticPool',
    'ElasticPoolUpdate',
    'FirewallRule',
    'GeoBackupPolicy',
    'ImportExtensionRequest',
    'ImportExportResponse',
    'ImportRequest',
    'ExportRequest',
    'MetricValue',
    'MetricName',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'ReplicationLink',
    'ServerAzureADAdministrator',
    'ServerCommunicationLink',
    'ServiceObjective',
    'ServerUsage',
    'DatabaseUsage',
    'DatabaseBlobAuditingPolicy',
    'AutomaticTuningOptions',
    'DatabaseAutomaticTuning',
    'EncryptionProtector',
    'FailoverGroupReadWriteEndpoint',
    'FailoverGroupReadOnlyEndpoint',
    'PartnerInfo',
    'FailoverGroup',
    'FailoverGroupUpdate',
    'OperationDisplay',
    'Operation',
    'ServerKey',
    'ResourceIdentity',
    'Server',
    'ServerUpdate',
    'SyncAgent',
    'SyncAgentKeyProperties',
    'SyncAgentLinkedDatabase',
    'SyncDatabaseIdProperties',
    'SyncFullSchemaTableColumn',
    'SyncFullSchemaTable',
    'SyncFullSchemaProperties',
    'SyncGroupLogProperties',
    'SyncGroupSchemaTableColumn',
    'SyncGroupSchemaTable',
    'SyncGroupSchema',
    'SyncGroup',
    'SyncMember',
    'SubscriptionUsage',
    'VirtualNetworkRule',
    'DatabaseOperation',
    'ResourceMoveDefinition',
    'AutomaticTuningServerOptions',
    'ServerAutomaticTuning',
    'ServerDnsAlias',
    'ServerDnsAliasAcquisition',
    'BackupLongTermRetentionPolicyPaged',
    'BackupLongTermRetentionVaultPaged',
    'RestorePointPaged',
    'RecoverableDatabasePaged',
    'RestorableDroppedDatabasePaged',
    'ServerPaged',
    'DatabasePaged',
    'MetricPaged',
    'MetricDefinitionPaged',
    'DataMaskingRulePaged',
    'ElasticPoolPaged',
    'FirewallRulePaged',
    'GeoBackupPolicyPaged',
    'ReplicationLinkPaged',
    'ServerAzureADAdministratorPaged',
    'ServerCommunicationLinkPaged',
    'ServiceObjectivePaged',
    'ElasticPoolActivityPaged',
    'ElasticPoolDatabaseActivityPaged',
    'RecommendedElasticPoolPaged',
    'RecommendedElasticPoolMetricPaged',
    'ServiceTierAdvisorPaged',
    'TransparentDataEncryptionActivityPaged',
    'ServerUsagePaged',
    'DatabaseUsagePaged',
    'EncryptionProtectorPaged',
    'FailoverGroupPaged',
    'OperationPaged',
    'ServerKeyPaged',
    'SyncAgentPaged',
    'SyncAgentLinkedDatabasePaged',
    'SyncDatabaseIdPropertiesPaged',
    'SyncFullSchemaPropertiesPaged',
    'SyncGroupLogPropertiesPaged',
    'SyncGroupPaged',
    'SyncMemberPaged',
    'SubscriptionUsagePaged',
    'VirtualNetworkRulePaged',
    'DatabaseOperationPaged',
    'ServerDnsAliasPaged',
    'BackupLongTermRetentionPolicyState',
    'RestorePointType',
    'CapabilityStatus',
    'MaxSizeUnits',
    'PerformanceLevelUnit',
    'CheckNameAvailabilityReason',
    'ServerConnectionType',
    'CreateMode',
    'DatabaseEdition',
    'ServiceObjectiveName',
    'TransparentDataEncryptionStatus',
    'RecommendedIndexAction',
    'RecommendedIndexState',
    'RecommendedIndexType',
    'ReadScale',
    'SampleName',
    'TransparentDataEncryptionActivityStatus',
    'ElasticPoolEdition',
    'SecurityAlertPolicyState',
    'SecurityAlertPolicyEmailAccountAdmins',
    'SecurityAlertPolicyUseServerDefault',
    'DataMaskingState',
    'DataMaskingRuleState',
    'DataMaskingFunction',
    'ElasticPoolState',
    'GeoBackupPolicyState',
    'StorageKeyType',
    'AuthenticationType',
    'UnitType',
    'PrimaryAggregationType',
    'UnitDefinitionType',
    'ReplicationRole',
    'ReplicationState',
    'BlobAuditingPolicyState',
    'AutomaticTuningMode',
    'AutomaticTuningOptionModeDesired',
    'AutomaticTuningOptionModeActual',
    'AutomaticTuningDisabledReason',
    'ServerKeyType',
    'ReadWriteEndpointFailoverPolicy',
    'ReadOnlyEndpointFailoverPolicy',
    'FailoverGroupReplicationRole',
    'OperationOrigin',
    'IdentityType',
    'SyncAgentState',
    'SyncMemberDbType',
    'SyncGroupLogType',
    'SyncConflictResolutionPolicy',
    'SyncGroupState',
    'SyncDirection',
    'SyncMemberState',
    'VirtualNetworkRuleState',
    'ManagementOperationState',
    'AutomaticTuningServerMode',
    'AutomaticTuningServerReason',
]
