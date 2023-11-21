from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Owner:
    username: str
    name: str
    url: str


@dataclass
class Archive:
    name: str
    url: str


@dataclass
class License:
    name: str
    url: str


@dataclass
class Connector:
    path: str
    slug: str
    uniqueId: str
    logo: object
    name: str
    title: str
    description: str
    owner: Owner
    support: str
    archive: Optional[Archive]
    license: Optional[List[License]]
    version: str
    versions: List[str]
    documentation_url: str
    source_url: str
    verification: str
    enterprise_support: str
    component_types: List
    cloud_availability: bool
    license_type: str


def jsonToDataclasses(json):
    connectors = []
    for c in json:
        archive_dc = None if not c['archive'] else Archive(name=c['archive']['name'], url=c['archive']['url'])
        licenses_dc = None if not c['license'] else [License(name=l['name'], url=l['url']) for l in c['license']]
        connectors.append(
            Connector(
                path=c['path'],
                slug=c['slug'],
                uniqueId=c['uniqueId'],
                logo=c['logo'], # shouldn't need so leaving as a JSON string
                name=c['name'],
                title=c['title'],
                description=c['description'],
                owner=Owner(username=c['owner']['username'], name=c['owner']['name'], url=c['owner']['url']),
                support=c['support'],
                archive=archive_dc,
                license=licenses_dc,
                version=c['version'],
                versions=[v for v in c['versions']],
                documentation_url=c['documentation_url'],
                source_url=c['source_url'],
                verification=c['verification'],
                enterprise_support=c['enterprise_support'],
                component_types=c['component_types'],
                cloud_availability=c['cloud_availability'],
                license_type=c['license_type']
            )
        )
    return connectors
