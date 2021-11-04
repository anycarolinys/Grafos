#include <iostream>
#include <list>
#include <queue>
#include <stack>
#include "BuscasGrafo.hpp"

using namespace std;

Grafo :: Grafo(int maximoVertices) {
    this->maximoVertices = maximoVertices;
    this->quantidadeVertices = 0;
    
    this->marcador = new bool[maximoVertices];
    this->listaAdjacencias = new list<pair<string, int>>[maximoVertices+1];
}

void Grafo :: reiniciaMarcador() {
    for (int i = 0; i < maximoVertices; i++) {
        marcador[i] = false;
    }
}

bool Grafo :: insereVertice(string nome, double preco) {
    if (quantidadeVertices >= maximoVertices)
        return false;

    Vertice novoVertice;
    novoVertice.nome = nome;
    novoVertice.preco = preco;
    novoVertice.posicaoLista = quantidadeVertices;

    vertices.push_back(novoVertice);
    quantidadeVertices++;
    return true;
}

bool Grafo :: insereAresta(string origem, string destino, int peso) {
    int posicaoOrigem = -1, posicaoDestino = -1;
    vector<Vertice> :: iterator vertice = vertices.begin();

    for (auto && vertice : vertices) {
        if(vertice.nome == origem) {
            posicaoOrigem = vertice.posicaoLista;
            break;
        }
    }

    for (auto && vertice : vertices) {
        if(vertice.nome == destino) {
            posicaoDestino = vertice.posicaoLista;
            break;
        }
    }
    
    // cout << "Posicao destino" << posicaoDestino << endl;
    // cout << "Posicao origem" << posicaoOrigem << endl;

    if (posicaoDestino != -1 && posicaoOrigem != -1) {
        listaAdjacencias[posicaoOrigem].push_back(make_pair(destino,peso));
        listaAdjacencias[posicaoDestino].push_back(make_pair(origem, peso));
        return true;
    }
    
    return false;
}

void Grafo :: imprimirVertices() {
    vector<Vertice> :: iterator i;

    for(i = vertices.begin(); i != vertices.end(); i++) {
        cout << "Nome: " << i->nome << endl;
        cout << "Preco: " << i->preco << endl;
        // cout << "Posicao no vetor: " << i->posicaoLista << endl;
    }

    cout << endl;
}

void Grafo :: imprimirListaAdjacencias() {
    vector<Vertice> :: iterator v;
    list<pair<string, int>> :: iterator adj;

    int i = 0;
    for(v = vertices.begin(); v != vertices.end(); v++) {
        cout << v->nome << " - ";
        for(adj = listaAdjacencias[i].begin(); adj != listaAdjacencias[i].end(); adj++) {
            cout << adj->first << "(" << adj->second << ") -> ";
        }
        cout << endl;
        i++;
    }
}

Vertice Grafo:: buscaVertice(string nomeVertice) {
    Vertice v;
    for (auto && vertice : vertices) {
        if (vertice.nome == nomeVertice) {
            v = vertice;
        }
    }
    return v;
}

void Grafo :: buscaLargura(Vertice origem, Vertice destino) {
    queue<Vertice> fila;
    bool encontrado = false;
    reiniciaMarcador();

    fila.push(origem);
    marcador[origem.posicaoLista] = true;

    // list<pair<string, int>> :: iterator adjacente;
    do
    {
        Vertice atual = fila.front();
        cout << atual.nome << " desenfileirado!" << endl;
        fila.pop();

        if (atual.nome == destino.nome && atual.preco == destino.preco) {
            cout << "Visitando " << atual.nome << endl;
            cout << "Destino encontrado!" << endl << endl;
            encontrado = true;
        } else {
            cout << endl << "Visitando " << atual.nome << endl;
            
            for (auto && adj : listaAdjacencias[atual.posicaoLista]) {
                Vertice adjacente = buscaVertice(adj.first);
                if (!marcador[adjacente.posicaoLista]) {
                    cout << "Enfileirando " << adjacente.nome << endl;
                    fila.push(adjacente);
                    marcador[adjacente.posicaoLista] = true; 
                }
            }
        }
    } while (!encontrado && !fila.empty());
    
    if (!encontrado)
        cout << "Caminho não encontrado!" << endl;
}

void Grafo :: buscaProfundidade(Vertice origem, Vertice destino) {
    stack<Vertice> pilha;
    reiniciaMarcador();

    pilha.push(origem);
    marcador[origem.posicaoLista] = true;

    bool encontrado = false;


    do {
        Vertice atual = pilha.top();
        pilha.pop();

        if (atual.nome == destino.nome && atual.preco == destino.preco) {
            cout << "Visitando " << atual.nome << endl;
            cout << "Destino encontrado!" << endl;
            encontrado = true;
        } else {
            cout << "Visitando " << atual.nome << endl;

            for (auto && adj : listaAdjacencias[atual.posicaoLista]) {
                Vertice adjacente = buscaVertice(adj.first);
                if (!marcador[adjacente.posicaoLista]) {
                    // cout << "Empilhando " << adjacente.nome << endl;
                    pilha.push(adjacente);
                    marcador[adjacente.posicaoLista] = true;
                }
            }
        }

    } while (!encontrado && !pilha.empty());
    
    if (!encontrado)
        cout << "Caminho não encontrado!" << endl;

}