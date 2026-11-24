"""Independent synthetic concept-catalogue demonstration."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Concept:
    title: str
    status: str
    tags: tuple[str, ...]

def search(records: list[Concept], query: str, status: str | None = None) -> list[Concept]:
    allowed = {"hypothesis", "conceptual", "illustrative"}
    if status is not None and status not in allowed:
        raise ValueError("Unknown status")
    for record in records:
        if record.status not in allowed or not record.title.strip():
            raise ValueError("Invalid record")
    term = query.strip().casefold()
    return [r for r in records if (status is None or r.status == status)
            and (not term or term in r.title.casefold() or any(term in tag.casefold() for tag in r.tags))]

if __name__ == "__main__":
    records = [Concept("Fictional concept A", "hypothesis", ("learning",)), Concept("Fictional concept B", "illustrative", ("systems",))]
    print(search(records, "learning"))
