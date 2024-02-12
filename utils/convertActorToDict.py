from services.getActorPictureById import getActorPictureById

def convert_actor_to_dict(actor):
    name = actor.get('name', '') if hasattr(actor, 'get') else ''
    role = actor.currentRole if hasattr(actor, 'currentRole') and not isinstance(actor.currentRole, list) else ', '.join(map(str, getattr(actor, 'currentRole', [])))
    note = getattr(actor, 'notes', '')
    id = actor.personID

    return {
        'name': name,
        'role': role if isinstance(role, str) else role.get('name', ''),
        'note': note,
        'img': getActorPictureById(id)
    }