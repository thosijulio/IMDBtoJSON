def convert_actor_to_dict(actor):
    name = actor.get('name', '') if hasattr(actor, 'get') else ''
    role = actor.currentRole if hasattr(actor, 'currentRole') and not isinstance(actor.currentRole, list) else ', '.join(map(str, getattr(actor, 'currentRole', [])))
    note = getattr(actor, 'notes', '')

    return {
        'name': name,
        'role': role if isinstance(role, str) else role.get('name', ''),
        'note': note
    }