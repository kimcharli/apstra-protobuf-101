from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_STATE_IS_ACTIVE: _ClassVar[DeviceState]
    DEVICE_STATE_IS_READY: _ClassVar[DeviceState]
    DEVICE_STATE_IS_NOCOMMS: _ClassVar[DeviceState]
    DEVICE_STATE_IS_MAINT: _ClassVar[DeviceState]
    DEVICE_STATE_IS_REBOOTING: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_STOCKED: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_QUARANTINED: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_READY: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_NOCOMMS: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_DECOMM: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_MAINT: _ClassVar[DeviceState]
    DEVICE_STATE_OOS_REBOOTING: _ClassVar[DeviceState]
    DEVICE_STATE_ERROR: _ClassVar[DeviceState]

class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_UNKNOWN: _ClassVar[Feature]
    FEATURE_LO0: _ClassVar[Feature]
    FEATURE_FABRIC: _ClassVar[Feature]
    FEATURE_LEAF_SERVER: _ClassVar[Feature]
    FEATURE_L3EDGE: _ClassVar[Feature]
    FEATURE_L2EDGE: _ClassVar[Feature]
    FEATURE_SPINE_LEAF: _ClassVar[Feature]
    FEATURE_FABRIC_SPINE: _ClassVar[Feature]
    FEATURE_EXTERNAL_ROUTER: _ClassVar[Feature]
    FEATURE_TO_EXTERNAL_ROUTER: _ClassVar[Feature]
    FEATURE_LEAF_L3_SERVER: _ClassVar[Feature]
    FEATURE_LEAF_L2_SERVER: _ClassVar[Feature]
    FEATURE_LEAF: _ClassVar[Feature]
    FEATURE_SPINE: _ClassVar[Feature]
    FEATURE_L3_SERVER: _ClassVar[Feature]
    FEATURE_L2_SERVER: _ClassVar[Feature]
    FEATURE_SERVER: _ClassVar[Feature]
    FEATURE_PEER: _ClassVar[Feature]
    FEATURE_LEAF_PEER_LINK: _ClassVar[Feature]
    FEATURE_LEAF_PAIR: _ClassVar[Feature]
    FEATURE_LEAF_PAIR_L2_SERVER: _ClassVar[Feature]
    FEATURE_UNUSED: _ClassVar[Feature]

class StreamingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAMING_TYPE_PERFMON: _ClassVar[StreamingType]
    STREAMING_TYPE_EVENTS: _ClassVar[StreamingType]
    STREAMING_TYPE_ALERTS: _ClassVar[StreamingType]

class StreamingProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAMING_PROTOCOL_PROTOBUF_OVER_TCP: _ClassVar[StreamingProtocol]

class StreamingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAMING_STATUS_UP: _ClassVar[StreamingStatus]
    STREAMING_STATUS_DOWN: _ClassVar[StreamingStatus]

class StreamingSequencingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAMING_UNSEQUENCED: _ClassVar[StreamingSequencingMode]
    STREAMING_SEQUENCED: _ClassVar[StreamingSequencingMode]

class BgpSessionAddressFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IPV4: _ClassVar[BgpSessionAddressFamily]
    IPV6: _ClassVar[BgpSessionAddressFamily]
    EVPN: _ClassVar[BgpSessionAddressFamily]

class LinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINK_UP: _ClassVar[LinkStatus]
    LINK_DOWN: _ClassVar[LinkStatus]
    LINK_UNKNOWN: _ClassVar[LinkStatus]
    LINK_MISSING: _ClassVar[LinkStatus]

class MacState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAC_ADD: _ClassVar[MacState]
    MAC_DELETE: _ClassVar[MacState]
    MAC_MOVE: _ClassVar[MacState]

class ArpState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARP_ADD: _ClassVar[ArpState]
    ARP_DELETE: _ClassVar[ArpState]

class MlagDomainState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLAG_UNKNOWN: _ClassVar[MlagDomainState]
    MLAG_MISSING: _ClassVar[MlagDomainState]
    MLAG_DISABLED: _ClassVar[MlagDomainState]
    MLAG_INACTIVE: _ClassVar[MlagDomainState]
    MLAG_ACTIVE: _ClassVar[MlagDomainState]

class MlagIntfState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLAG_INTF_UNKNOWN: _ClassVar[MlagIntfState]
    MLAG_INTF_MISSING: _ClassVar[MlagIntfState]
    MLAG_INTF_DISABLED: _ClassVar[MlagIntfState]
    MLAG_INTF_CONFIGURED: _ClassVar[MlagIntfState]
    MLAG_INTF_INACTIVE: _ClassVar[MlagIntfState]
    MLAG_INTF_ACTIVE_PARTIAL: _ClassVar[MlagIntfState]
    MLAG_INTF_ACTIVE_FULL: _ClassVar[MlagIntfState]

class RouteState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_ADD: _ClassVar[RouteState]
    ROUTE_DELETE: _ClassVar[RouteState]

class AlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_LOW: _ClassVar[AlertSeverity]
    ALERT_MEDIUM: _ClassVar[AlertSeverity]
    ALERT_HIGH: _ClassVar[AlertSeverity]
    ALERT_CRITICAL: _ClassVar[AlertSeverity]

class RouteEntryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_ENTRY_STATUS_UNKNOWN: _ClassVar[RouteEntryStatus]
    ROUTE_ENTRY_STATUS_UP: _ClassVar[RouteEntryStatus]
    ROUTE_ENTRY_STATUS_PARTIAL: _ClassVar[RouteEntryStatus]
    ROUTE_ENTRY_STATUS_MISSING: _ClassVar[RouteEntryStatus]

class NextHopStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEXT_HOP_STATUS_UNKNOWN: _ClassVar[NextHopStatus]
    NEXT_HOP_STATUS_UP: _ClassVar[NextHopStatus]
    NEXT_HOP_STATUS_MISSING: _ClassVar[NextHopStatus]

class RouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_TYPE_UNKNOWN: _ClassVar[RouteType]
    ROUTE_TYPE_DIRECT: _ClassVar[RouteType]
    ROUTE_TYPE_BGP: _ClassVar[RouteType]
    ROUTE_TYPE_STAT: _ClassVar[RouteType]

class DeploymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_STATUS_INPROGRESS: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_SUCCEEDED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_FAILED: _ClassVar[DeploymentStatus]

class StreamingAlertReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAMING_ALERT_REASON_FAILED_CONNECTION: _ClassVar[StreamingAlertReason]
    STREAMING_ALERT_REASON_TIMEOUT: _ClassVar[StreamingAlertReason]
    STREAMING_ALERT_REASON_DNS_FAILURE: _ClassVar[StreamingAlertReason]
    STREAMING_ALERT_REASON_WRITE_TIMEOUT: _ClassVar[StreamingAlertReason]

class BgpSessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BGP_SESSION_UP: _ClassVar[BgpSessionState]
    BGP_SESSION_DOWN: _ClassVar[BgpSessionState]
    BGP_SESSION_MISSING: _ClassVar[BgpSessionState]
    BGP_SESSION_UNKNOWN: _ClassVar[BgpSessionState]

class AggregationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGGREGATION_TYPE_MAX: _ClassVar[AggregationType]
    AGGREGATION_TYPE_MIN: _ClassVar[AggregationType]
    AGGREGATION_TYPE_SUM: _ClassVar[AggregationType]
    AGGREGATION_TYPE_AVG: _ClassVar[AggregationType]
    AGGREGATION_TYPE_STD: _ClassVar[AggregationType]

class HeadroomType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEADROOM_TYPE_MAX: _ClassVar[HeadroomType]
    HEADROOM_TYPE_MIN: _ClassVar[HeadroomType]
DEVICE_STATE_IS_ACTIVE: DeviceState
DEVICE_STATE_IS_READY: DeviceState
DEVICE_STATE_IS_NOCOMMS: DeviceState
DEVICE_STATE_IS_MAINT: DeviceState
DEVICE_STATE_IS_REBOOTING: DeviceState
DEVICE_STATE_OOS_STOCKED: DeviceState
DEVICE_STATE_OOS_QUARANTINED: DeviceState
DEVICE_STATE_OOS_READY: DeviceState
DEVICE_STATE_OOS_NOCOMMS: DeviceState
DEVICE_STATE_OOS_DECOMM: DeviceState
DEVICE_STATE_OOS_MAINT: DeviceState
DEVICE_STATE_OOS_REBOOTING: DeviceState
DEVICE_STATE_ERROR: DeviceState
FEATURE_UNKNOWN: Feature
FEATURE_LO0: Feature
FEATURE_FABRIC: Feature
FEATURE_LEAF_SERVER: Feature
FEATURE_L3EDGE: Feature
FEATURE_L2EDGE: Feature
FEATURE_SPINE_LEAF: Feature
FEATURE_FABRIC_SPINE: Feature
FEATURE_EXTERNAL_ROUTER: Feature
FEATURE_TO_EXTERNAL_ROUTER: Feature
FEATURE_LEAF_L3_SERVER: Feature
FEATURE_LEAF_L2_SERVER: Feature
FEATURE_LEAF: Feature
FEATURE_SPINE: Feature
FEATURE_L3_SERVER: Feature
FEATURE_L2_SERVER: Feature
FEATURE_SERVER: Feature
FEATURE_PEER: Feature
FEATURE_LEAF_PEER_LINK: Feature
FEATURE_LEAF_PAIR: Feature
FEATURE_LEAF_PAIR_L2_SERVER: Feature
FEATURE_UNUSED: Feature
STREAMING_TYPE_PERFMON: StreamingType
STREAMING_TYPE_EVENTS: StreamingType
STREAMING_TYPE_ALERTS: StreamingType
STREAMING_PROTOCOL_PROTOBUF_OVER_TCP: StreamingProtocol
STREAMING_STATUS_UP: StreamingStatus
STREAMING_STATUS_DOWN: StreamingStatus
STREAMING_UNSEQUENCED: StreamingSequencingMode
STREAMING_SEQUENCED: StreamingSequencingMode
IPV4: BgpSessionAddressFamily
IPV6: BgpSessionAddressFamily
EVPN: BgpSessionAddressFamily
LINK_UP: LinkStatus
LINK_DOWN: LinkStatus
LINK_UNKNOWN: LinkStatus
LINK_MISSING: LinkStatus
MAC_ADD: MacState
MAC_DELETE: MacState
MAC_MOVE: MacState
ARP_ADD: ArpState
ARP_DELETE: ArpState
MLAG_UNKNOWN: MlagDomainState
MLAG_MISSING: MlagDomainState
MLAG_DISABLED: MlagDomainState
MLAG_INACTIVE: MlagDomainState
MLAG_ACTIVE: MlagDomainState
MLAG_INTF_UNKNOWN: MlagIntfState
MLAG_INTF_MISSING: MlagIntfState
MLAG_INTF_DISABLED: MlagIntfState
MLAG_INTF_CONFIGURED: MlagIntfState
MLAG_INTF_INACTIVE: MlagIntfState
MLAG_INTF_ACTIVE_PARTIAL: MlagIntfState
MLAG_INTF_ACTIVE_FULL: MlagIntfState
ROUTE_ADD: RouteState
ROUTE_DELETE: RouteState
ALERT_LOW: AlertSeverity
ALERT_MEDIUM: AlertSeverity
ALERT_HIGH: AlertSeverity
ALERT_CRITICAL: AlertSeverity
ROUTE_ENTRY_STATUS_UNKNOWN: RouteEntryStatus
ROUTE_ENTRY_STATUS_UP: RouteEntryStatus
ROUTE_ENTRY_STATUS_PARTIAL: RouteEntryStatus
ROUTE_ENTRY_STATUS_MISSING: RouteEntryStatus
NEXT_HOP_STATUS_UNKNOWN: NextHopStatus
NEXT_HOP_STATUS_UP: NextHopStatus
NEXT_HOP_STATUS_MISSING: NextHopStatus
ROUTE_TYPE_UNKNOWN: RouteType
ROUTE_TYPE_DIRECT: RouteType
ROUTE_TYPE_BGP: RouteType
ROUTE_TYPE_STAT: RouteType
DEPLOYMENT_STATUS_INPROGRESS: DeploymentStatus
DEPLOYMENT_STATUS_SUCCEEDED: DeploymentStatus
DEPLOYMENT_STATUS_FAILED: DeploymentStatus
STREAMING_ALERT_REASON_FAILED_CONNECTION: StreamingAlertReason
STREAMING_ALERT_REASON_TIMEOUT: StreamingAlertReason
STREAMING_ALERT_REASON_DNS_FAILURE: StreamingAlertReason
STREAMING_ALERT_REASON_WRITE_TIMEOUT: StreamingAlertReason
BGP_SESSION_UP: BgpSessionState
BGP_SESSION_DOWN: BgpSessionState
BGP_SESSION_MISSING: BgpSessionState
BGP_SESSION_UNKNOWN: BgpSessionState
AGGREGATION_TYPE_MAX: AggregationType
AGGREGATION_TYPE_MIN: AggregationType
AGGREGATION_TYPE_SUM: AggregationType
AGGREGATION_TYPE_AVG: AggregationType
AGGREGATION_TYPE_STD: AggregationType
HEADROOM_TYPE_MAX: HeadroomType
HEADROOM_TYPE_MIN: HeadroomType

class DeviceStateEvent(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: DeviceState
    def __init__(self, state: _Optional[_Union[DeviceState, str]] = ...) -> None: ...

class TrafficEvent(_message.Message):
    __slots__ = ("node_role", "port_role", "port", "node", "pod", "interval_seconds", "measurement_name", "aggregation_type", "delta_percentage", "delta_nonnormalized")
    NODE_ROLE_FIELD_NUMBER: _ClassVar[int]
    PORT_ROLE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    DELTA_NONNORMALIZED_FIELD_NUMBER: _ClassVar[int]
    node_role: Feature
    port_role: Feature
    port: str
    node: str
    pod: bool
    interval_seconds: int
    measurement_name: str
    aggregation_type: AggregationType
    delta_percentage: int
    delta_nonnormalized: int
    def __init__(self, node_role: _Optional[_Union[Feature, str]] = ..., port_role: _Optional[_Union[Feature, str]] = ..., port: _Optional[str] = ..., node: _Optional[str] = ..., pod: bool = ..., interval_seconds: _Optional[int] = ..., measurement_name: _Optional[str] = ..., aggregation_type: _Optional[_Union[AggregationType, str]] = ..., delta_percentage: _Optional[int] = ..., delta_nonnormalized: _Optional[int] = ...) -> None: ...

class StreamingEvent(_message.Message):
    __slots__ = ("aos_server", "streaming_type", "protocol", "status", "sequencing_mode")
    AOS_SERVER_FIELD_NUMBER: _ClassVar[int]
    STREAMING_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_MODE_FIELD_NUMBER: _ClassVar[int]
    aos_server: str
    streaming_type: StreamingType
    protocol: StreamingProtocol
    status: StreamingStatus
    sequencing_mode: StreamingSequencingMode
    def __init__(self, aos_server: _Optional[str] = ..., streaming_type: _Optional[_Union[StreamingType, str]] = ..., protocol: _Optional[_Union[StreamingProtocol, str]] = ..., status: _Optional[_Union[StreamingStatus, str]] = ..., sequencing_mode: _Optional[_Union[StreamingSequencingMode, str]] = ...) -> None: ...

class CablePeerEvent(_message.Message):
    __slots__ = ("lcl_device_id", "lcl_hostname", "lcl_ifname", "rmt_hostname", "rmt_ifname", "rmt_sysdescr")
    LCL_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    LCL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LCL_IFNAME_FIELD_NUMBER: _ClassVar[int]
    RMT_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    RMT_IFNAME_FIELD_NUMBER: _ClassVar[int]
    RMT_SYSDESCR_FIELD_NUMBER: _ClassVar[int]
    lcl_device_id: str
    lcl_hostname: str
    lcl_ifname: str
    rmt_hostname: str
    rmt_ifname: str
    rmt_sysdescr: str
    def __init__(self, lcl_device_id: _Optional[str] = ..., lcl_hostname: _Optional[str] = ..., lcl_ifname: _Optional[str] = ..., rmt_hostname: _Optional[str] = ..., rmt_ifname: _Optional[str] = ..., rmt_sysdescr: _Optional[str] = ...) -> None: ...

class BGPNeighborEvent(_message.Message):
    __slots__ = ("lcl_hostname", "lcl_ipaddr", "lcl_asn", "state", "rmt_ipaddr", "rmt_asn", "vrf_name", "addr_family")
    LCL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LCL_IPADDR_FIELD_NUMBER: _ClassVar[int]
    LCL_ASN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RMT_IPADDR_FIELD_NUMBER: _ClassVar[int]
    RMT_ASN_FIELD_NUMBER: _ClassVar[int]
    VRF_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDR_FAMILY_FIELD_NUMBER: _ClassVar[int]
    lcl_hostname: str
    lcl_ipaddr: str
    lcl_asn: int
    state: BgpSessionState
    rmt_ipaddr: str
    rmt_asn: int
    vrf_name: str
    addr_family: BgpSessionAddressFamily
    def __init__(self, lcl_hostname: _Optional[str] = ..., lcl_ipaddr: _Optional[str] = ..., lcl_asn: _Optional[int] = ..., state: _Optional[_Union[BgpSessionState, str]] = ..., rmt_ipaddr: _Optional[str] = ..., rmt_asn: _Optional[int] = ..., vrf_name: _Optional[str] = ..., addr_family: _Optional[_Union[BgpSessionAddressFamily, str]] = ...) -> None: ...

class LinkStatusEvent(_message.Message):
    __slots__ = ("hostname", "ifname", "state")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IFNAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    ifname: str
    state: LinkStatus
    def __init__(self, hostname: _Optional[str] = ..., ifname: _Optional[str] = ..., state: _Optional[_Union[LinkStatus, str]] = ...) -> None: ...

class MacEvent(_message.Message):
    __slots__ = ("macaddress", "intfname", "vlan", "state")
    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTFNAME_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    macaddress: str
    intfname: str
    vlan: int
    state: MacState
    def __init__(self, macaddress: _Optional[str] = ..., intfname: _Optional[str] = ..., vlan: _Optional[int] = ..., state: _Optional[_Union[MacState, str]] = ...) -> None: ...

class ArpEvent(_message.Message):
    __slots__ = ("ipaddress", "mac", "intfname", "state", "vrfname")
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    INTFNAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VRFNAME_FIELD_NUMBER: _ClassVar[int]
    ipaddress: str
    mac: str
    intfname: str
    state: ArpState
    vrfname: str
    def __init__(self, ipaddress: _Optional[str] = ..., mac: _Optional[str] = ..., intfname: _Optional[str] = ..., state: _Optional[_Union[ArpState, str]] = ..., vrfname: _Optional[str] = ...) -> None: ...

class LagEvent(_message.Message):
    __slots__ = ("hostname", "lagname", "interfacesupcount", "interfacesup")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LAGNAME_FIELD_NUMBER: _ClassVar[int]
    INTERFACESUPCOUNT_FIELD_NUMBER: _ClassVar[int]
    INTERFACESUP_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    lagname: str
    interfacesupcount: int
    interfacesup: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hostname: _Optional[str] = ..., lagname: _Optional[str] = ..., interfacesupcount: _Optional[int] = ..., interfacesup: _Optional[_Iterable[str]] = ...) -> None: ...

class MlagEvent(_message.Message):
    __slots__ = ("domain_id", "domain_state", "intfname", "intf_state")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    INTFNAME_FIELD_NUMBER: _ClassVar[int]
    INTF_STATE_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    domain_state: MlagDomainState
    intfname: str
    intf_state: MlagIntfState
    def __init__(self, domain_id: _Optional[str] = ..., domain_state: _Optional[_Union[MlagDomainState, str]] = ..., intfname: _Optional[str] = ..., intf_state: _Optional[_Union[MlagIntfState, str]] = ...) -> None: ...

class ExtensibleServiceEvent(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class RouteEvent(_message.Message):
    __slots__ = ("dest_network", "status", "hostname")
    DEST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    dest_network: str
    status: RouteEntryStatus
    hostname: str
    def __init__(self, dest_network: _Optional[str] = ..., status: _Optional[_Union[RouteEntryStatus, str]] = ..., hostname: _Optional[str] = ...) -> None: ...

class EvpnType3RouteEvent(_message.Message):
    __slots__ = ("state", "system_id", "vni", "next_hop", "rd", "rt")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    VNI_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
    RD_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    state: RouteState
    system_id: str
    vni: int
    next_hop: str
    rd: str
    rt: str
    def __init__(self, state: _Optional[_Union[RouteState, str]] = ..., system_id: _Optional[str] = ..., vni: _Optional[int] = ..., next_hop: _Optional[str] = ..., rd: _Optional[str] = ..., rt: _Optional[str] = ...) -> None: ...

class ActiveFloodlistEvent(_message.Message):
    __slots__ = ("state", "system_id", "vni", "vtep")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    VNI_FIELD_NUMBER: _ClassVar[int]
    VTEP_FIELD_NUMBER: _ClassVar[int]
    state: RouteState
    system_id: str
    vni: int
    vtep: str
    def __init__(self, state: _Optional[_Union[RouteState, str]] = ..., system_id: _Optional[str] = ..., vni: _Optional[int] = ..., vtep: _Optional[str] = ...) -> None: ...

class EvpnType5RouteEvent(_message.Message):
    __slots__ = ("state", "system_id", "af", "subnet", "next_hop", "rd", "rt")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    AF_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
    RD_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    state: RouteState
    system_id: str
    af: str
    subnet: str
    next_hop: str
    rd: str
    rt: str
    def __init__(self, state: _Optional[_Union[RouteState, str]] = ..., system_id: _Optional[str] = ..., af: _Optional[str] = ..., subnet: _Optional[str] = ..., next_hop: _Optional[str] = ..., rd: _Optional[str] = ..., rt: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("id", "device_state", "streaming", "cable_peer", "bgp_neighbor", "link_status", "traffic", "mac_state", "arp_state", "lag_state", "mlag_state", "extensible_event", "route_state")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    STREAMING_FIELD_NUMBER: _ClassVar[int]
    CABLE_PEER_FIELD_NUMBER: _ClassVar[int]
    BGP_NEIGHBOR_FIELD_NUMBER: _ClassVar[int]
    LINK_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    MAC_STATE_FIELD_NUMBER: _ClassVar[int]
    ARP_STATE_FIELD_NUMBER: _ClassVar[int]
    LAG_STATE_FIELD_NUMBER: _ClassVar[int]
    MLAG_STATE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIBLE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_state: DeviceStateEvent
    streaming: StreamingEvent
    cable_peer: CablePeerEvent
    bgp_neighbor: BGPNeighborEvent
    link_status: LinkStatusEvent
    traffic: TrafficEvent
    mac_state: MacEvent
    arp_state: ArpEvent
    lag_state: LagEvent
    mlag_state: MlagEvent
    extensible_event: ExtensibleServiceEvent
    route_state: RouteEvent
    def __init__(self, id: _Optional[str] = ..., device_state: _Optional[_Union[DeviceStateEvent, _Mapping]] = ..., streaming: _Optional[_Union[StreamingEvent, _Mapping]] = ..., cable_peer: _Optional[_Union[CablePeerEvent, _Mapping]] = ..., bgp_neighbor: _Optional[_Union[BGPNeighborEvent, _Mapping]] = ..., link_status: _Optional[_Union[LinkStatusEvent, _Mapping]] = ..., traffic: _Optional[_Union[TrafficEvent, _Mapping]] = ..., mac_state: _Optional[_Union[MacEvent, _Mapping]] = ..., arp_state: _Optional[_Union[ArpEvent, _Mapping]] = ..., lag_state: _Optional[_Union[LagEvent, _Mapping]] = ..., mlag_state: _Optional[_Union[MlagEvent, _Mapping]] = ..., extensible_event: _Optional[_Union[ExtensibleServiceEvent, _Mapping]] = ..., route_state: _Optional[_Union[RouteEvent, _Mapping]] = ...) -> None: ...

class HostnameAlert(_message.Message):
    __slots__ = ("expected_hostname", "actual_hostname")
    EXPECTED_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    expected_hostname: str
    actual_hostname: str
    def __init__(self, expected_hostname: _Optional[str] = ..., actual_hostname: _Optional[str] = ...) -> None: ...

class ConfigDeviationAlert(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LivenessAlert(_message.Message):
    __slots__ = ("expected_agents", "actual_agents", "alive")
    EXPECTED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_AGENTS_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    expected_agents: _containers.RepeatedScalarFieldContainer[str]
    actual_agents: _containers.RepeatedScalarFieldContainer[str]
    alive: bool
    def __init__(self, expected_agents: _Optional[_Iterable[str]] = ..., actual_agents: _Optional[_Iterable[str]] = ..., alive: bool = ...) -> None: ...

class ExtensibleAlert(_message.Message):
    __slots__ = ("key", "expected", "actual")
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_FIELD_NUMBER: _ClassVar[int]
    key: str
    expected: str
    actual: str
    def __init__(self, key: _Optional[str] = ..., expected: _Optional[str] = ..., actual: _Optional[str] = ...) -> None: ...

class DeploymentAlert(_message.Message):
    __slots__ = ("expected_deployment_status", "actual_deployment_status")
    EXPECTED_DEPLOYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DEPLOYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    expected_deployment_status: DeploymentStatus
    actual_deployment_status: DeploymentStatus
    def __init__(self, expected_deployment_status: _Optional[_Union[DeploymentStatus, str]] = ..., actual_deployment_status: _Optional[_Union[DeploymentStatus, str]] = ...) -> None: ...

class BlueprintRenderingAlert(_message.Message):
    __slots__ = ("failed_systems",)
    FAILED_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    failed_systems: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, failed_systems: _Optional[_Iterable[str]] = ...) -> None: ...

class RouteAlert(_message.Message):
    __slots__ = ("ip", "expected_dest_status", "actual_dest_status")
    IP_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ip: str
    expected_dest_status: RouteEntryStatus
    actual_dest_status: RouteEntryStatus
    def __init__(self, ip: _Optional[str] = ..., expected_dest_status: _Optional[_Union[RouteEntryStatus, str]] = ..., actual_dest_status: _Optional[_Union[RouteEntryStatus, str]] = ...) -> None: ...

class LagAlert(_message.Message):
    __slots__ = ("hostname", "lagname", "expected_ifup_count", "actual_ifup_count", "expected_interfaces_up", "actual_interfaces_up")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LAGNAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_IFUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_IFUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_INTERFACES_UP_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_INTERFACES_UP_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    lagname: str
    expected_ifup_count: int
    actual_ifup_count: int
    expected_interfaces_up: _containers.RepeatedScalarFieldContainer[str]
    actual_interfaces_up: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hostname: _Optional[str] = ..., lagname: _Optional[str] = ..., expected_ifup_count: _Optional[int] = ..., actual_ifup_count: _Optional[int] = ..., expected_interfaces_up: _Optional[_Iterable[str]] = ..., actual_interfaces_up: _Optional[_Iterable[str]] = ...) -> None: ...

class StreamingAlert(_message.Message):
    __slots__ = ("aos_server", "streaming_type", "protocol", "reason", "sequencing_mode")
    AOS_SERVER_FIELD_NUMBER: _ClassVar[int]
    STREAMING_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_MODE_FIELD_NUMBER: _ClassVar[int]
    aos_server: str
    streaming_type: StreamingType
    protocol: StreamingProtocol
    reason: StreamingAlertReason
    sequencing_mode: StreamingSequencingMode
    def __init__(self, aos_server: _Optional[str] = ..., streaming_type: _Optional[_Union[StreamingType, str]] = ..., protocol: _Optional[_Union[StreamingProtocol, str]] = ..., reason: _Optional[_Union[StreamingAlertReason, str]] = ..., sequencing_mode: _Optional[_Union[StreamingSequencingMode, str]] = ...) -> None: ...

class CablePeerMismatchAlert(_message.Message):
    __slots__ = ("lcl_hostname", "lcl_ifname", "exp_hostname", "exp_ifname", "rmt_hostname", "rmt_ifname", "rmt_sysdescr")
    LCL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LCL_IFNAME_FIELD_NUMBER: _ClassVar[int]
    EXP_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    EXP_IFNAME_FIELD_NUMBER: _ClassVar[int]
    RMT_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    RMT_IFNAME_FIELD_NUMBER: _ClassVar[int]
    RMT_SYSDESCR_FIELD_NUMBER: _ClassVar[int]
    lcl_hostname: str
    lcl_ifname: str
    exp_hostname: str
    exp_ifname: str
    rmt_hostname: str
    rmt_ifname: str
    rmt_sysdescr: str
    def __init__(self, lcl_hostname: _Optional[str] = ..., lcl_ifname: _Optional[str] = ..., exp_hostname: _Optional[str] = ..., exp_ifname: _Optional[str] = ..., rmt_hostname: _Optional[str] = ..., rmt_ifname: _Optional[str] = ..., rmt_sysdescr: _Optional[str] = ...) -> None: ...

class BGPNeighborMismatchAlert(_message.Message):
    __slots__ = ("lcl_hostname", "lcl_ipaddr", "lcl_asn", "rmt_ipaddr", "rmt_asn", "expected_state", "actual_state", "rmt_name", "vrf_name", "addr_family")
    LCL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LCL_IPADDR_FIELD_NUMBER: _ClassVar[int]
    LCL_ASN_FIELD_NUMBER: _ClassVar[int]
    RMT_IPADDR_FIELD_NUMBER: _ClassVar[int]
    RMT_ASN_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_STATE_FIELD_NUMBER: _ClassVar[int]
    RMT_NAME_FIELD_NUMBER: _ClassVar[int]
    VRF_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDR_FAMILY_FIELD_NUMBER: _ClassVar[int]
    lcl_hostname: str
    lcl_ipaddr: str
    lcl_asn: int
    rmt_ipaddr: str
    rmt_asn: int
    expected_state: BgpSessionState
    actual_state: BgpSessionState
    rmt_name: str
    vrf_name: str
    addr_family: BgpSessionAddressFamily
    def __init__(self, lcl_hostname: _Optional[str] = ..., lcl_ipaddr: _Optional[str] = ..., lcl_asn: _Optional[int] = ..., rmt_ipaddr: _Optional[str] = ..., rmt_asn: _Optional[int] = ..., expected_state: _Optional[_Union[BgpSessionState, str]] = ..., actual_state: _Optional[_Union[BgpSessionState, str]] = ..., rmt_name: _Optional[str] = ..., vrf_name: _Optional[str] = ..., addr_family: _Optional[_Union[BgpSessionAddressFamily, str]] = ...) -> None: ...

class InterfaceLinkStatusMismatchAlert(_message.Message):
    __slots__ = ("hostname", "ifname", "expected_ifstatus", "actual_ifstatus")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IFNAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_IFSTATUS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_IFSTATUS_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    ifname: str
    expected_ifstatus: LinkStatus
    actual_ifstatus: LinkStatus
    def __init__(self, hostname: _Optional[str] = ..., ifname: _Optional[str] = ..., expected_ifstatus: _Optional[_Union[LinkStatus, str]] = ..., actual_ifstatus: _Optional[_Union[LinkStatus, str]] = ...) -> None: ...

class CountersAlert(_message.Message):
    __slots__ = ("node_role", "port_role", "port", "node", "pod", "measurement_name", "interval_seconds", "aggregation_type")
    NODE_ROLE_FIELD_NUMBER: _ClassVar[int]
    PORT_ROLE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    node_role: Feature
    port_role: Feature
    port: str
    node: str
    pod: bool
    measurement_name: str
    interval_seconds: int
    aggregation_type: AggregationType
    def __init__(self, node_role: _Optional[_Union[Feature, str]] = ..., port_role: _Optional[_Union[Feature, str]] = ..., port: _Optional[str] = ..., node: _Optional[str] = ..., pod: bool = ..., measurement_name: _Optional[str] = ..., interval_seconds: _Optional[int] = ..., aggregation_type: _Optional[_Union[AggregationType, str]] = ...) -> None: ...

class KeyValuePair(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ProbeAlert(_message.Message):
    __slots__ = ("expected_int", "actual_int", "expected_float", "actual_float", "expected_discrete_state", "actual_discrete_state", "probe_id", "stage_name", "key_value_pairs", "item_id", "expected_text", "actual_text", "probe_label", "expected_int_max", "expected_float_max")
    EXPECTED_INT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_INT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DISCRETE_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DISCRETE_STATE_FIELD_NUMBER: _ClassVar[int]
    PROBE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_PAIRS_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    PROBE_LABEL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_INT_MAX_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FLOAT_MAX_FIELD_NUMBER: _ClassVar[int]
    expected_int: int
    actual_int: int
    expected_float: float
    actual_float: float
    expected_discrete_state: str
    actual_discrete_state: str
    probe_id: str
    stage_name: str
    key_value_pairs: _containers.RepeatedCompositeFieldContainer[KeyValuePair]
    item_id: str
    expected_text: str
    actual_text: str
    probe_label: str
    expected_int_max: int
    expected_float_max: float
    def __init__(self, expected_int: _Optional[int] = ..., actual_int: _Optional[int] = ..., expected_float: _Optional[float] = ..., actual_float: _Optional[float] = ..., expected_discrete_state: _Optional[str] = ..., actual_discrete_state: _Optional[str] = ..., probe_id: _Optional[str] = ..., stage_name: _Optional[str] = ..., key_value_pairs: _Optional[_Iterable[_Union[KeyValuePair, _Mapping]]] = ..., item_id: _Optional[str] = ..., expected_text: _Optional[str] = ..., actual_text: _Optional[str] = ..., probe_label: _Optional[str] = ..., expected_int_max: _Optional[int] = ..., expected_float_max: _Optional[float] = ...) -> None: ...

class ConfigMismatchAlert(_message.Message):
    __slots__ = ("blueprint_id", "collector_id")
    BLUEPRINT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    blueprint_id: str
    collector_id: str
    def __init__(self, blueprint_id: _Optional[str] = ..., collector_id: _Optional[str] = ...) -> None: ...

class HeadroomAlert(_message.Message):
    __slots__ = ("node_a", "node_b", "interval_seconds", "headroom_type")
    NODE_A_FIELD_NUMBER: _ClassVar[int]
    NODE_B_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HEADROOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    node_a: str
    node_b: str
    interval_seconds: int
    headroom_type: HeadroomType
    def __init__(self, node_a: _Optional[str] = ..., node_b: _Optional[str] = ..., interval_seconds: _Optional[int] = ..., headroom_type: _Optional[_Union[HeadroomType, str]] = ...) -> None: ...

class MacAlert(_message.Message):
    __slots__ = ("macaddress", "intfname", "vlan", "movecount", "actual_move_interval", "expected_max_interval")
    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTFNAME_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    MOVECOUNT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_MOVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_MAX_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    macaddress: str
    intfname: str
    vlan: int
    movecount: int
    actual_move_interval: float
    expected_max_interval: float
    def __init__(self, macaddress: _Optional[str] = ..., intfname: _Optional[str] = ..., vlan: _Optional[int] = ..., movecount: _Optional[int] = ..., actual_move_interval: _Optional[float] = ..., expected_max_interval: _Optional[float] = ...) -> None: ...

class ArpAlert(_message.Message):
    __slots__ = ("ipaddress", "mac", "intfname")
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    INTFNAME_FIELD_NUMBER: _ClassVar[int]
    ipaddress: str
    mac: str
    intfname: str
    def __init__(self, ipaddress: _Optional[str] = ..., mac: _Optional[str] = ..., intfname: _Optional[str] = ...) -> None: ...

class MlagAlert(_message.Message):
    __slots__ = ("hostname", "domain_id", "mlag_id", "expected_domain_state", "actual_domain_state", "ifname", "expected_intf_state", "actual_intf_state", "peer_link", "peer_link_status", "expected_peer_link_status")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MLAG_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    IFNAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_INTF_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_INTF_STATE_FIELD_NUMBER: _ClassVar[int]
    PEER_LINK_FIELD_NUMBER: _ClassVar[int]
    PEER_LINK_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PEER_LINK_STATUS_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    domain_id: str
    mlag_id: int
    expected_domain_state: MlagDomainState
    actual_domain_state: MlagDomainState
    ifname: str
    expected_intf_state: MlagIntfState
    actual_intf_state: MlagIntfState
    peer_link: str
    peer_link_status: str
    expected_peer_link_status: str
    def __init__(self, hostname: _Optional[str] = ..., domain_id: _Optional[str] = ..., mlag_id: _Optional[int] = ..., expected_domain_state: _Optional[_Union[MlagDomainState, str]] = ..., actual_domain_state: _Optional[_Union[MlagDomainState, str]] = ..., ifname: _Optional[str] = ..., expected_intf_state: _Optional[_Union[MlagIntfState, str]] = ..., actual_intf_state: _Optional[_Union[MlagIntfState, str]] = ..., peer_link: _Optional[str] = ..., peer_link_status: _Optional[str] = ..., expected_peer_link_status: _Optional[str] = ...) -> None: ...

class TestAlert(_message.Message):
    __slots__ = ("test_int",)
    TEST_INT_FIELD_NUMBER: _ClassVar[int]
    test_int: int
    def __init__(self, test_int: _Optional[int] = ...) -> None: ...

class InterfaceCounters(_message.Message):
    __slots__ = ("tx_unicast_packets", "tx_broadcast_packets", "tx_multicast_packets", "tx_bytes", "rx_unicast_packets", "rx_broadcast_packets", "rx_multicast_packets", "rx_bytes", "tx_error_packets", "tx_discard_packets", "rx_error_packets", "rx_discard_packets", "alignment_errors", "fcs_errors", "symbol_errors", "runts", "giants", "delta_seconds", "delta_microseconds")
    TX_UNICAST_PACKETS_FIELD_NUMBER: _ClassVar[int]
    TX_BROADCAST_PACKETS_FIELD_NUMBER: _ClassVar[int]
    TX_MULTICAST_PACKETS_FIELD_NUMBER: _ClassVar[int]
    TX_BYTES_FIELD_NUMBER: _ClassVar[int]
    RX_UNICAST_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RX_BROADCAST_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RX_MULTICAST_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RX_BYTES_FIELD_NUMBER: _ClassVar[int]
    TX_ERROR_PACKETS_FIELD_NUMBER: _ClassVar[int]
    TX_DISCARD_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RX_ERROR_PACKETS_FIELD_NUMBER: _ClassVar[int]
    RX_DISCARD_PACKETS_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_ERRORS_FIELD_NUMBER: _ClassVar[int]
    FCS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    RUNTS_FIELD_NUMBER: _ClassVar[int]
    GIANTS_FIELD_NUMBER: _ClassVar[int]
    DELTA_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DELTA_MICROSECONDS_FIELD_NUMBER: _ClassVar[int]
    tx_unicast_packets: int
    tx_broadcast_packets: int
    tx_multicast_packets: int
    tx_bytes: int
    rx_unicast_packets: int
    rx_broadcast_packets: int
    rx_multicast_packets: int
    rx_bytes: int
    tx_error_packets: int
    tx_discard_packets: int
    rx_error_packets: int
    rx_discard_packets: int
    alignment_errors: int
    fcs_errors: int
    symbol_errors: int
    runts: int
    giants: int
    delta_seconds: int
    delta_microseconds: int
    def __init__(self, tx_unicast_packets: _Optional[int] = ..., tx_broadcast_packets: _Optional[int] = ..., tx_multicast_packets: _Optional[int] = ..., tx_bytes: _Optional[int] = ..., rx_unicast_packets: _Optional[int] = ..., rx_broadcast_packets: _Optional[int] = ..., rx_multicast_packets: _Optional[int] = ..., rx_bytes: _Optional[int] = ..., tx_error_packets: _Optional[int] = ..., tx_discard_packets: _Optional[int] = ..., rx_error_packets: _Optional[int] = ..., rx_discard_packets: _Optional[int] = ..., alignment_errors: _Optional[int] = ..., fcs_errors: _Optional[int] = ..., symbol_errors: _Optional[int] = ..., runts: _Optional[int] = ..., giants: _Optional[int] = ..., delta_seconds: _Optional[int] = ..., delta_microseconds: _Optional[int] = ...) -> None: ...

class SystemInfo(_message.Message):
    __slots__ = ("cpu_user", "cpu_system", "cpu_idle", "memory_used", "memory_total")
    CPU_USER_FIELD_NUMBER: _ClassVar[int]
    CPU_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    CPU_IDLE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TOTAL_FIELD_NUMBER: _ClassVar[int]
    cpu_user: float
    cpu_system: float
    cpu_idle: float
    memory_used: int
    memory_total: int
    def __init__(self, cpu_user: _Optional[float] = ..., cpu_system: _Optional[float] = ..., cpu_idle: _Optional[float] = ..., memory_used: _Optional[int] = ..., memory_total: _Optional[int] = ...) -> None: ...

class ProcessInfo(_message.Message):
    __slots__ = ("process_name", "cpu_user", "cpu_system", "memory_used")
    PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
    CPU_USER_FIELD_NUMBER: _ClassVar[int]
    CPU_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_FIELD_NUMBER: _ClassVar[int]
    process_name: str
    cpu_user: float
    cpu_system: float
    memory_used: int
    def __init__(self, process_name: _Optional[str] = ..., cpu_user: _Optional[float] = ..., cpu_system: _Optional[float] = ..., memory_used: _Optional[int] = ...) -> None: ...

class FileInfo(_message.Message):
    __slots__ = ("file_name", "file_size")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_size: int
    def __init__(self, file_name: _Optional[str] = ..., file_size: _Optional[int] = ...) -> None: ...

class SysResourceCounters(_message.Message):
    __slots__ = ("system_info", "process_info", "file_info")
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    system_info: SystemInfo
    process_info: _containers.RepeatedCompositeFieldContainer[ProcessInfo]
    file_info: _containers.RepeatedCompositeFieldContainer[FileInfo]
    def __init__(self, system_info: _Optional[_Union[SystemInfo, _Mapping]] = ..., process_info: _Optional[_Iterable[_Union[ProcessInfo, _Mapping]]] = ..., file_info: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("name", "int64_value", "float_value", "string_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    int64_value: int
    float_value: float
    string_value: str
    def __init__(self, name: _Optional[str] = ..., int64_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("name", "int64_value", "float_value", "string_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    int64_value: int
    float_value: float
    string_value: str
    def __init__(self, name: _Optional[str] = ..., int64_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ...) -> None: ...

class ProbeProperty(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class InterfaceCountersUtilization(_message.Message):
    __slots__ = ("tx_utilization", "rx_utilization", "tx_unicast_pps", "tx_broadcast_pps", "tx_multicast_pps", "tx_bps", "tx_error_pps", "tx_discard_pps", "rx_unicast_pps", "rx_broadcast_pps", "rx_multicast_pps", "rx_bps", "rx_error_pps", "rx_discard_pps", "alignment_errors_per_second", "fcs_errors_per_second", "symbol_errors_per_second", "runts_per_second", "giants_per_second")
    TX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    RX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    TX_UNICAST_PPS_FIELD_NUMBER: _ClassVar[int]
    TX_BROADCAST_PPS_FIELD_NUMBER: _ClassVar[int]
    TX_MULTICAST_PPS_FIELD_NUMBER: _ClassVar[int]
    TX_BPS_FIELD_NUMBER: _ClassVar[int]
    TX_ERROR_PPS_FIELD_NUMBER: _ClassVar[int]
    TX_DISCARD_PPS_FIELD_NUMBER: _ClassVar[int]
    RX_UNICAST_PPS_FIELD_NUMBER: _ClassVar[int]
    RX_BROADCAST_PPS_FIELD_NUMBER: _ClassVar[int]
    RX_MULTICAST_PPS_FIELD_NUMBER: _ClassVar[int]
    RX_BPS_FIELD_NUMBER: _ClassVar[int]
    RX_ERROR_PPS_FIELD_NUMBER: _ClassVar[int]
    RX_DISCARD_PPS_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_ERRORS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    FCS_ERRORS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_ERRORS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    RUNTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    GIANTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    tx_utilization: int
    rx_utilization: int
    tx_unicast_pps: int
    tx_broadcast_pps: int
    tx_multicast_pps: int
    tx_bps: int
    tx_error_pps: int
    tx_discard_pps: int
    rx_unicast_pps: int
    rx_broadcast_pps: int
    rx_multicast_pps: int
    rx_bps: int
    rx_error_pps: int
    rx_discard_pps: int
    alignment_errors_per_second: int
    fcs_errors_per_second: int
    symbol_errors_per_second: int
    runts_per_second: int
    giants_per_second: int
    def __init__(self, tx_utilization: _Optional[int] = ..., rx_utilization: _Optional[int] = ..., tx_unicast_pps: _Optional[int] = ..., tx_broadcast_pps: _Optional[int] = ..., tx_multicast_pps: _Optional[int] = ..., tx_bps: _Optional[int] = ..., tx_error_pps: _Optional[int] = ..., tx_discard_pps: _Optional[int] = ..., rx_unicast_pps: _Optional[int] = ..., rx_broadcast_pps: _Optional[int] = ..., rx_multicast_pps: _Optional[int] = ..., rx_bps: _Optional[int] = ..., rx_error_pps: _Optional[int] = ..., rx_discard_pps: _Optional[int] = ..., alignment_errors_per_second: _Optional[int] = ..., fcs_errors_per_second: _Optional[int] = ..., symbol_errors_per_second: _Optional[int] = ..., runts_per_second: _Optional[int] = ..., giants_per_second: _Optional[int] = ...) -> None: ...

class SystemInterfaceUtilization(_message.Message):
    __slots__ = ("aggregate_tx_bps", "aggregate_rx_bps", "max_ifc_tx_utilization", "max_ifc_rx_utilization", "aggregate_tx_utilization", "aggregate_rx_utilization")
    AGGREGATE_TX_BPS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_RX_BPS_FIELD_NUMBER: _ClassVar[int]
    MAX_IFC_TX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MAX_IFC_RX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_TX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_RX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    aggregate_tx_bps: int
    aggregate_rx_bps: int
    max_ifc_tx_utilization: int
    max_ifc_rx_utilization: int
    aggregate_tx_utilization: int
    aggregate_rx_utilization: int
    def __init__(self, aggregate_tx_bps: _Optional[int] = ..., aggregate_rx_bps: _Optional[int] = ..., max_ifc_tx_utilization: _Optional[int] = ..., max_ifc_rx_utilization: _Optional[int] = ..., aggregate_tx_utilization: _Optional[int] = ..., aggregate_rx_utilization: _Optional[int] = ...) -> None: ...

class ProbeMessage(_message.Message):
    __slots__ = ("property", "int64_value", "float_value", "string_value", "evpn_type3_route_state", "evpn_type5_route_state", "interface_counters_utilization", "system_interface_utilization", "active_floodlist", "probe_id", "stage_name", "blueprint_id", "item_id", "probe_label")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    EVPN_TYPE3_ROUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    EVPN_TYPE5_ROUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_COUNTERS_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INTERFACE_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FLOODLIST_FIELD_NUMBER: _ClassVar[int]
    PROBE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PROBE_LABEL_FIELD_NUMBER: _ClassVar[int]
    property: _containers.RepeatedCompositeFieldContainer[ProbeProperty]
    int64_value: int
    float_value: float
    string_value: str
    evpn_type3_route_state: EvpnType3RouteEvent
    evpn_type5_route_state: EvpnType5RouteEvent
    interface_counters_utilization: InterfaceCountersUtilization
    system_interface_utilization: SystemInterfaceUtilization
    active_floodlist: ActiveFloodlistEvent
    probe_id: str
    stage_name: str
    blueprint_id: str
    item_id: str
    probe_label: str
    def __init__(self, property: _Optional[_Iterable[_Union[ProbeProperty, _Mapping]]] = ..., int64_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ..., evpn_type3_route_state: _Optional[_Union[EvpnType3RouteEvent, _Mapping]] = ..., evpn_type5_route_state: _Optional[_Union[EvpnType5RouteEvent, _Mapping]] = ..., interface_counters_utilization: _Optional[_Union[InterfaceCountersUtilization, _Mapping]] = ..., system_interface_utilization: _Optional[_Union[SystemInterfaceUtilization, _Mapping]] = ..., active_floodlist: _Optional[_Union[ActiveFloodlistEvent, _Mapping]] = ..., probe_id: _Optional[str] = ..., stage_name: _Optional[str] = ..., blueprint_id: _Optional[str] = ..., item_id: _Optional[str] = ..., probe_label: _Optional[str] = ...) -> None: ...

class GenericPerfmonMessage(_message.Message):
    __slots__ = ("tags", "fields")
    TAGS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class ProbeData(_message.Message):
    __slots__ = ("tags", "fields")
    TAGS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class PerfMon(_message.Message):
    __slots__ = ("interface_counters", "system_resource_counters", "generic", "probe_message", "time_delta")
    INTERFACE_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    GENERIC_FIELD_NUMBER: _ClassVar[int]
    PROBE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_DELTA_FIELD_NUMBER: _ClassVar[int]
    interface_counters: InterfaceCounters
    system_resource_counters: SysResourceCounters
    generic: GenericPerfmonMessage
    probe_message: ProbeMessage
    time_delta: float
    def __init__(self, interface_counters: _Optional[_Union[InterfaceCounters, _Mapping]] = ..., system_resource_counters: _Optional[_Union[SysResourceCounters, _Mapping]] = ..., generic: _Optional[_Union[GenericPerfmonMessage, _Mapping]] = ..., probe_message: _Optional[_Union[ProbeMessage, _Mapping]] = ..., time_delta: _Optional[float] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("severity", "first_seen", "id", "raised", "config_deviation_alert", "streaming_alert", "cable_peer_mismatch_alert", "bgp_neighbor_mismatch_alert", "interface_link_status_mismatch_alert", "hostname_alert", "route_alert", "liveness_alert", "deployment_alert", "blueprint_rendering_alert", "counters_alert", "mac_alert", "arp_alert", "headroom_alert", "lag_alert", "mlag_alert", "probe_alert", "config_mismatch_alert", "extensible_alert", "test_alert")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RAISED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_DEVIATION_ALERT_FIELD_NUMBER: _ClassVar[int]
    STREAMING_ALERT_FIELD_NUMBER: _ClassVar[int]
    CABLE_PEER_MISMATCH_ALERT_FIELD_NUMBER: _ClassVar[int]
    BGP_NEIGHBOR_MISMATCH_ALERT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_LINK_STATUS_MISMATCH_ALERT_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_ALERT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ALERT_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_ALERT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ALERT_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_RENDERING_ALERT_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_ALERT_FIELD_NUMBER: _ClassVar[int]
    MAC_ALERT_FIELD_NUMBER: _ClassVar[int]
    ARP_ALERT_FIELD_NUMBER: _ClassVar[int]
    HEADROOM_ALERT_FIELD_NUMBER: _ClassVar[int]
    LAG_ALERT_FIELD_NUMBER: _ClassVar[int]
    MLAG_ALERT_FIELD_NUMBER: _ClassVar[int]
    PROBE_ALERT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MISMATCH_ALERT_FIELD_NUMBER: _ClassVar[int]
    EXTENSIBLE_ALERT_FIELD_NUMBER: _ClassVar[int]
    TEST_ALERT_FIELD_NUMBER: _ClassVar[int]
    severity: AlertSeverity
    first_seen: int
    id: str
    raised: bool
    config_deviation_alert: ConfigDeviationAlert
    streaming_alert: StreamingAlert
    cable_peer_mismatch_alert: CablePeerMismatchAlert
    bgp_neighbor_mismatch_alert: BGPNeighborMismatchAlert
    interface_link_status_mismatch_alert: InterfaceLinkStatusMismatchAlert
    hostname_alert: HostnameAlert
    route_alert: RouteAlert
    liveness_alert: LivenessAlert
    deployment_alert: DeploymentAlert
    blueprint_rendering_alert: BlueprintRenderingAlert
    counters_alert: CountersAlert
    mac_alert: MacAlert
    arp_alert: ArpAlert
    headroom_alert: HeadroomAlert
    lag_alert: LagAlert
    mlag_alert: MlagAlert
    probe_alert: ProbeAlert
    config_mismatch_alert: ConfigMismatchAlert
    extensible_alert: ExtensibleAlert
    test_alert: TestAlert
    def __init__(self, severity: _Optional[_Union[AlertSeverity, str]] = ..., first_seen: _Optional[int] = ..., id: _Optional[str] = ..., raised: bool = ..., config_deviation_alert: _Optional[_Union[ConfigDeviationAlert, _Mapping]] = ..., streaming_alert: _Optional[_Union[StreamingAlert, _Mapping]] = ..., cable_peer_mismatch_alert: _Optional[_Union[CablePeerMismatchAlert, _Mapping]] = ..., bgp_neighbor_mismatch_alert: _Optional[_Union[BGPNeighborMismatchAlert, _Mapping]] = ..., interface_link_status_mismatch_alert: _Optional[_Union[InterfaceLinkStatusMismatchAlert, _Mapping]] = ..., hostname_alert: _Optional[_Union[HostnameAlert, _Mapping]] = ..., route_alert: _Optional[_Union[RouteAlert, _Mapping]] = ..., liveness_alert: _Optional[_Union[LivenessAlert, _Mapping]] = ..., deployment_alert: _Optional[_Union[DeploymentAlert, _Mapping]] = ..., blueprint_rendering_alert: _Optional[_Union[BlueprintRenderingAlert, _Mapping]] = ..., counters_alert: _Optional[_Union[CountersAlert, _Mapping]] = ..., mac_alert: _Optional[_Union[MacAlert, _Mapping]] = ..., arp_alert: _Optional[_Union[ArpAlert, _Mapping]] = ..., headroom_alert: _Optional[_Union[HeadroomAlert, _Mapping]] = ..., lag_alert: _Optional[_Union[LagAlert, _Mapping]] = ..., mlag_alert: _Optional[_Union[MlagAlert, _Mapping]] = ..., probe_alert: _Optional[_Union[ProbeAlert, _Mapping]] = ..., config_mismatch_alert: _Optional[_Union[ConfigMismatchAlert, _Mapping]] = ..., extensible_alert: _Optional[_Union[ExtensibleAlert, _Mapping]] = ..., test_alert: _Optional[_Union[TestAlert, _Mapping]] = ...) -> None: ...

class AosMessage(_message.Message):
    __slots__ = ("timestamp", "origin_name", "origin_hostname", "origin_role", "blueprint_label", "alert", "event", "perf_mon")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ROLE_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_LABEL_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PERF_MON_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    origin_name: str
    origin_hostname: str
    origin_role: str
    blueprint_label: str
    alert: Alert
    event: Event
    perf_mon: PerfMon
    def __init__(self, timestamp: _Optional[int] = ..., origin_name: _Optional[str] = ..., origin_hostname: _Optional[str] = ..., origin_role: _Optional[str] = ..., blueprint_label: _Optional[str] = ..., alert: _Optional[_Union[Alert, _Mapping]] = ..., event: _Optional[_Union[Event, _Mapping]] = ..., perf_mon: _Optional[_Union[PerfMon, _Mapping]] = ...) -> None: ...

class AosSequencedMessage(_message.Message):
    __slots__ = ("seq_num", "aos_proto")
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    AOS_PROTO_FIELD_NUMBER: _ClassVar[int]
    seq_num: int
    aos_proto: bytes
    def __init__(self, seq_num: _Optional[int] = ..., aos_proto: _Optional[bytes] = ...) -> None: ...
