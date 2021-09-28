import pytest
from django.urls import reverse
from random import randrange


@pytest.mark.django_db
def test_course_detail(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=(course.id,))
    response = client.get(url)

    assert response.status_code == 200
    assert course.name == response.data['name']


@pytest.mark.django_db
def test_course_list(client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-list')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    courses = course_factory(_quantity=3)
    course = courses[randrange(0, len(courses))]
    url = reverse('courses-detail', args=(course.id,))
    params = {'id': course.id}
    response = client.get(url, params)

    assert response.status_code == 200
    assert course.id == response.data['id']


@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    courses = course_factory(_quantity=3)
    course = courses[randrange(0, len(courses))]
    url = reverse('courses-detail', args=(course.id,))
    params = {'name': course.name}
    response = client.get(url, params)

    assert response.status_code == 200
    assert course.name == response.data['name']


@pytest.mark.django_db
def test_create_course(client):
    payload = {
        'name': 'Python in Web Development'
    }
    url = reverse('courses-list')
    response = client.post(url, data=payload)

    assert response.status_code == 201
    assert response.data['name'] == payload['name']


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=(course.id,))
    payload = {
        'name': 'Django'
    }
    response = client.patch(url, data=payload)

    assert response.status_code == 200
    assert response.data['name'] == payload['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=(course.id,))
    response = client.delete(url)

    assert response.status_code == 204
