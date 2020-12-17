# try it yourself. Perfect code for Github visualization 
import requests
from plotly.graph_objs import bar
from plotly import offline 

def get_response(language):
    """Make an API call to Github and return the reponse"""
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=star'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url,headers=headers)
    return r

def get_repo_dicts(r):
    """ Return a set of dicts representing the most popular repositories. """
    response_dict = r.json()
    return response_dict['items']
   
def get_project_data(repo_dicts):
    """Return data needed for each project in visualization."""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels

def make_visualization(repo_links, stars, labels):
    """Generate the visualization of most commented articles."""
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Most-Starred Python Projects on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },

    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')
    

if __name__ == '__main__':
    response = get_response('python')
    repo_dicts = get_repo_dicts(response)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)