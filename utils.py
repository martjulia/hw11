import json


def load_candidates_from_json():
    """– возвращает список всех кандидатов"""
    with open('candidates.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    data = load_candidates_from_json()
    for candidate in data:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """"возвращает кандидатов по имени"""
    data = load_candidates_from_json()
    candidates = []
    for candidate in data:
        if candidate_name in candidate['name']:
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    data = load_candidates_from_json()
    candidates = []
    for candidate in data:
        if skill_name in candidate['skills']:
            candidates.append(candidate)
    return candidates
