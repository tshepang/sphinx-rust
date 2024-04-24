from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType
from sphinx.roles import XRefRole

from .sphinx_rust import __version__, analyze_module

if TYPE_CHECKING:
    from docutils.nodes import Element
    from sphinx.addnodes import desc_signature, pending_xref
    from sphinx.application import Sphinx
    from sphinx.builders import Builder
    from sphinx.environment import BuildEnvironment
    from sphinx.util.typing import ExtensionMetadata

__all__ = ("__version__", "analyze_module", "setup")


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_domain(RustDomain)
    return {"version": __version__, "parallel_read_safe": True}


class RustModuleDirective(ObjectDescription[str]):
    """Directive to document a Rust module."""

    def handle_signature(self, sig: str, signode: desc_signature) -> str:  # noqa: PLR6301
        return sig

    def add_target_and_index(
        self, name: str, sig: str, signode: desc_signature
    ) -> None:
        pass


class RustStructDirective(ObjectDescription[str]):
    """Directive to document a Rust struct."""

    def handle_signature(self, sig: str, signode: desc_signature) -> str:  # noqa: PLR6301
        return sig

    def add_target_and_index(
        self, name: str, sig: str, signode: desc_signature
    ) -> None:
        pass


class RustFieldDirective(ObjectDescription[str]):
    """Directive to document a Rust struct field."""

    def handle_signature(self, sig: str, signode: desc_signature) -> str:  # noqa: PLR6301
        return sig

    def add_target_and_index(
        self, name: str, sig: str, signode: desc_signature
    ) -> None:
        pass


class RustModuleRole(XRefRole):
    """Role to cross-reference a Rust module."""


class RustStructRole(XRefRole):
    """Role to cross-reference a Rust struct."""


class RustFieldRole(XRefRole):
    """Role to cross-reference a Rust struct field."""


class RustDomain(Domain):
    """Rust domain."""

    name = "rust"
    label = "Rust"

    object_types = {
        "module": ObjType("module", "module"),
        "struct": ObjType("struct", "struct"),
        "field": ObjType("field", "field"),
    }

    directives = {
        "module": RustModuleDirective,
        "struct": RustStructDirective,
        "field": RustFieldDirective,
    }

    roles = {
        "module": RustModuleRole(),
        "struct": RustStructRole(),
        "field": RustFieldRole(),
    }

    def merge_domaindata(self, docnames: list[str], otherdata: dict[str, Any]) -> None:
        raise NotImplementedError  # TODO

    def resolve_any_xref(  # noqa: PLR0913, PLR6301, PLR0917
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> list[tuple[str, Element]]:
        return []
